from setuptools import setup, find_packages

setup(
 name = 'issue_reporter',
 version = '0.1.1',
 description = """Simple interface for quickly reporting issues with a GUI and Mailgun out the back""",
 packages = find_packages(),
 package_data={'issue_reporter': [
  'locale/*/*/*',
 ]},
 zip_safe = False,
 install_requires = ['sysinfo', 'mailgun_api'],
)
