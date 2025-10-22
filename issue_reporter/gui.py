import sys

import i18n_core
from gui_builder import fields
from wx_utils import forms as wx_forms

from . import issue_reporter

i18n_core.install_module_translation("issue_reporter", module=sys.modules["issue_reporter.gui"])


class IssueReporterDialog(wx_forms.AutoSizedDialog):
    email = fields.Text(
        label=__("Your &Email Address"),
        min_size=(500, 20),
        tool_tip_text=__("Your email address for follow-up questions"),
    )
    summary = fields.Text(label=__("Summary"), min_size=(500, 20), tool_tip_text=__("Brief description of the issue"))
    frequencies = ("Rarely", "Sometimes", "Frequently", "Always")
    frequency = fields.RadioButtonGroup(
        label=__("How frequently does the Issue occur?"),
        choices=[__("Rarely"), __("Sometimes"), __("Frequently"), __("Always")],
        tool_tip_text=__("How often you experience this issue"),
    )
    steps = fields.Text(
        label=__("Steps to Reproduce"),
        multiline=True,
        min_size=(500, 150),
        tool_tip_text=__("Detailed steps to reproduce the issue"),
    )
    expected = fields.Text(
        label=__("Expected Results"),
        multiline=True,
        min_size=(500, 150),
        tool_tip_text=__("What you expected to happen"),
    )
    actual = fields.Text(
        label=__("Actual Results"), multiline=True, min_size=(500, 150), tool_tip_text=__("What actually happened")
    )
    buttons = fields.ButtonSizer(ok=True, cancel=True)

    def get_report(self):
        frequency_index = self.frequency.get_index()
        assert frequency_index is not None, "Frequency selection is required"
        return issue_reporter.Report(
            email=self.email.get_value(),
            summary=self.summary.get_value(),
            frequency=self.frequencies[frequency_index],
            steps=self.steps.get_value(),
            expected_results=self.expected.get_value(),
            actual_results=self.actual.get_value(),
        )
