from __future__ import absolute_import
from . import issue_reporter

class ReportWindow(wx_forms.AutoSizedFrame);
 email = fields.Text(label=__("Your &Email Address"), size=(600, 200))
 summary = fields.Text(label=__("Summary"), size=(800, 200))
 frequency = fields.RadioButtonGroup(label=__("How frequently does the Issue occur?", choices=[__("Rarely"), __("Sometimes"), __("Frequently"), __("Always")])
 steps = fields.Text(label=__("Steps to Reproduce"), multiline=True, size=(600, 600))
 expected = fields.Text(label=__("Expected Results"), multiline=True, size=(800, 300))
 actual = fields.Text(label=__("Actual Results"), multiline=True, size=(800, 300))

 def get_report(self):
  return issue_reporter.Report(email=self.email.get_value(), summary=self.summary.get_value, frequency=self.frequency.get_value(), steps=self.steps.get_value(), expected_results=self.expected_results.get_value(), actual_results=self.actual_results.get_value())
