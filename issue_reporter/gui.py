from __future__ import absolute_import
from . import issue_reporter
from wx_utils import forms as wx_forms
from gui_builder import fields, forms

import sys
import i18n_core
i18n_core.install_module_translation('issue_reporter', module=sys.modules['issue_reporter.gui'])

class IssueReporterDialog(wx_forms.AutoSizedDialog):
 email = fields.Text(label=__("Your &Email Address"), size=(200, 20))
 summary = fields.Text(label=__("Summary"), size=(400, 20))
 frequencies = ("Rarely", "Sometimes", "Frequently", "Always")
 frequency = fields.RadioButtonGroup(label=__("How frequently does the Issue occur?"), choices=[__("Rarely"), __("Sometimes"), __("Frequently"), __("Always")])
 steps = fields.Text(label=__("Steps to Reproduce"), multiline=True, size=(400, 100))
 expected = fields.Text(label=__("Expected Results"), multiline=True, size=(400, 100))
 actual = fields.Text(label=__("Actual Results"), multiline=True, size=(400, 100))
 buttons = fields.ButtonSizer(ok=True, cancel=True)

 def get_report(self):
  return issue_reporter.Report(email=self.email.get_value(), summary=self.summary.get_value(), frequency=self.frequencies[self.frequency.get_index()], steps=self.steps.get_value(), expected_results=self.expected.get_value(), actual_results=self.actual.get_value())
