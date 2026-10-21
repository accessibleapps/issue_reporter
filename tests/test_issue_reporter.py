"""Assert real report behavior without services, host inventory, or real logs."""

import importlib.util
import io
import json
import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock, patch

import pytest


@pytest.fixture
def delivery():
    api = Mock()
    mailgun = ModuleType("mailgun_api")
    mailgun.MailgunAPI = Mock(return_value=api)
    inventory = ModuleType("sysinfo")
    inventory.system_info = Mock(side_effect=AssertionError("real host inventory is forbidden"))
    source = Path(__file__).parents[1] / "issue_reporter" / "issue_reporter.py"
    spec = importlib.util.spec_from_file_location("offline_issue_reporter", source)
    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, {"mailgun_api": mailgun, "sysinfo": inventory}):
        spec.loader.exec_module(module)
    return module, mailgun, inventory, api


def test_constructor_configures_mock_mailgun_with_sender_domain(delivery):
    module, mailgun, _, api = delivery
    reporter = module.IssueReporter(
        "sender@example.invalid", "support@example.invalid", mailgun_api_key="dummy-fixture-key"
    )

    mailgun.MailgunAPI.assert_called_once_with("dummy-fixture-key", "example.invalid")
    assert reporter.from_address == "sender@example.invalid"
    assert reporter.to_address == "support@example.invalid"
    assert reporter.mailgun_api is api


def test_explicit_system_info_avoids_inventory_collection(delivery):
    module, _, inventory, _ = delivery
    system_info = {"fixture": True}
    report = module.Report(system_info=system_info)

    assert report.system_info is system_info
    inventory.system_info.assert_not_called()


def test_missing_system_info_uses_mocked_inventory(delivery):
    module, _, inventory, _ = delivery
    inventory.system_info.side_effect = None
    inventory.system_info.return_value = {"fixture": "mock inventory"}
    report = module.Report()

    inventory.system_info.assert_called_once_with()
    assert report.system_info is inventory.system_info.return_value


def test_default_log_paths_are_independent(delivery):
    module, _, _, _ = delivery
    first = module.Report(system_info={})
    second = module.Report(system_info={})
    first.log_paths.append("fixture.log")

    assert second.log_paths == []


@pytest.mark.parametrize("log_paths", [[], ["fixture.log"]])
def test_send_report_formats_payload_and_closes_successful_attachments(delivery, monkeypatch, log_paths):
    module, _, inventory, api = delivery
    reporter = module.IssueReporter(
        "sender@example.invalid", "support@example.invalid", mailgun_api_key="dummy-fixture-key"
    )
    report = module.Report(
        system_info={"fixture": True},
        application_name="ExampleApp",
        application_version="1.0",
        email="reporter@example.invalid",
        summary="Fixture report",
        frequency="always",
        steps="Open fixture",
        expected_results="Expected fixture",
        actual_results="Actual fixture",
        log_paths=log_paths,
    )
    log = io.BytesIO(b"fixture log contents")
    file_open = Mock(return_value=log)
    monkeypatch.setattr(module, "open", file_open, raising=False)

    def inspect_payload(sender, recipient, **kwargs):
        assert (sender, recipient) == ("sender@example.invalid", "support@example.invalid")
        assert kwargs["subject"] == "ExampleApp: Fixture report"
        assert kwargs["text"] == (
            "Reporter: reporter@example.invalid\nVersion: 1.0\nFrequency: always\n"
            "Steps to reproduce:\nOpen fixture\n\nExpected Results:\nExpected fixture\n\n"
            "Actual Results:\nActual fixture\n"
        )
        assert kwargs["h:Reply-To"] == "<reporter@example.invalid>"
        assert kwargs["test"] is True
        assert kwargs["custom"] == "preserved"
        files = kwargs["files"]
        assert len(files) == 1 + len(log_paths)
        assert all(name == "attachment" for name, _ in files)
        assert files[0][1].name == "sysinfo.json"
        assert json.load(files[0][1]) == {"fixture": True}
        if log_paths:
            assert files[1][1] is log
            assert log.read() == b"fixture log contents"

    api.send_message.side_effect = inspect_payload
    reporter.send_report(report, test=True, custom="preserved")

    api.send_message.assert_called_once()
    assert all(file.closed for _, file in api.send_message.call_args.kwargs["files"])
    inventory.system_info.assert_not_called()
    if log_paths:
        file_open.assert_called_once_with("fixture.log", "rb")
    else:
        file_open.assert_not_called()
