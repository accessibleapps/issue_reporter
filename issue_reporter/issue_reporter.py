import json
from StringIO import StringIO #not cStringIO so we can set its name
import mailgun_api
import sysinfo


class Report(object):

 def __init__(self, system_info=None, application_name=None, email=None, summary=None, frequency=None, steps=None, expected_results=None, actual_results=None, log_paths=None):
  if system_info is None:
   system_info = sysinfo.system_info()
  self.system_info = system_info
  self.application_name = application_name
  self.email = email
  self.summary = summary
  self.frequency = frequency
  self.steps = steps
  self.expected_results = expected_results
  self.actual_results = actual_results
  if log_paths is None:
   log_paths = []
  self.log_paths = log_paths

class IssueReporter(object):
 message_template = """Reporter: {report.email}
Frequency: {report.frequency}
Steps to reproduce:
{report.steps}

Expected Results:
{report.expected_results}

Actual Results:
{report.actual_results}
"""
 

 def __init__(self, from_address, to_address, mailgun_api_key=None):
  self.from_address = from_address
  self.to_address = to_address
  domain = from_address.split('@')[1]
  self.mailgun_api = mailgun_api.MailgunAPI(mailgun_api_key, domain)

 def send_report(self, report, **kwargs):
  subject = report.application_name + ': ' + report.summary
  message = self.message_template.format(report=report)
  sysinfo = StringIO()
  json.dump(report.system_info, sysinfo, indent=2)
  sysinfo.seek(0)
  sysinfo.name = 'sysinfo.json'
  files = [('attachment', sysinfo)]
  for path in report.log_paths:
   files.append(('attachment', open(path, 'rb')))
  kwargs['h:Reply-To'] = "<"+report.email+">"
  self.mailgun_api.send_message(self.from_address, self.to_address, subject=subject, text=message, files=files, **kwargs)
  for f in files:
   f[1].close()

