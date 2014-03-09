import issue_reporter

def test_sending_a_fake_report():
 reporter = issue_reporter.IssueReporter(from_address='errors@q-continuum.net', to_address='q@q-continuum.net', mailgun_api_key='key-10k0owvah9n62asajwu487d4a139k6j0')
 report = issue_reporter.Report(
  email = 'q@q-continuum.net',
  summary = "It don't work",
  frequency = "All the time",
  steps = "Just run it",
  expected_results = "It works",
  actual_results = "It doesn't",
 )
 reporter.send_report(report, test=True)
