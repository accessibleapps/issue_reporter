"""Exercise real delivery code without importing service-bearing legacy tests."""

import importlib.util
import io
import json
import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock, patch

import pytest


@pytest.fixture
def delivery(monkeypatch):
    api = Mock()
    mailgun = ModuleType("mailgun_api")
    mailgun.MailgunAPI = Mock(return_value=api)
    sysinfo = ModuleType("sysinfo")
    sysinfo.system_info = Mock(side_effect=AssertionError("host inventory is forbidden"))
    source = Path(__file__).parents[1] / "issue_reporter" / "issue_reporter.py"
    spec = importlib.util.spec_from_file_location("report_delivery_under_test", source)
    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, {"mailgun_api": mailgun, "sysinfo": sysinfo}):
        spec.loader.exec_module(module)

    reporter = module.IssueReporter("sender@example.invalid", "support@example.invalid")
    report = module.Report(
        system_info={"fixture": True},
        application_name="ExampleApp",
        application_version="1.0",
        email="reporter@example.invalid",
        summary="Test report",
        log_paths=["application.log"],
    )
    attachment = io.BytesIO(b"fixture log")
    attachment.name = "application.log"
    monkeypatch.setattr(module, "open", Mock(return_value=attachment), raising=False)
    return reporter, report, attachment, api


def test_success_preserves_payload_and_closes_attachments(delivery):
    reporter, report, attachment, api = delivery

    def inspect_payload(from_address, to_address, **kwargs):
        assert (from_address, to_address) == ("sender@example.invalid", "support@example.invalid")
        assert kwargs["subject"] == "ExampleApp: Test report"
        assert kwargs["h:Reply-To"] == "<reporter@example.invalid>"
        assert kwargs["text"].startswith("Reporter: reporter@example.invalid\nVersion: 1.0\n")
        assert kwargs["custom"] == "preserved"
        files = kwargs["files"]
        assert [name for name, _ in files] == ["attachment", "attachment"]
        assert files[0][1].name == "sysinfo.json"
        assert json.load(files[0][1]) == {"fixture": True}
        assert files[1][1] is attachment
        assert attachment.read() == b"fixture log"

    api.send_message.side_effect = inspect_payload
    reporter.send_report(report, custom="preserved")

    api.send_message.assert_called_once()
    assert all(file.closed for _, file in api.send_message.call_args.kwargs["files"])


def test_delivery_failure_closes_attachments_and_preserves_exception(delivery):
    reporter, report, attachment, api = delivery
    failure = RuntimeError("fixture delivery failed")
    api.send_message.side_effect = failure

    with pytest.raises(RuntimeError) as caught:
        reporter.send_report(report)

    assert caught.value is failure
    assert attachment.closed
    assert all(file.closed for _, file in api.send_message.call_args.kwargs["files"])
