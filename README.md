# Issue Reporter

Issue Reporter is a Python library that provides a user-friendly GUI for reporting issues or bugs in applications. It simplifies the process of collecting, formatting, and sending issue reports via email using the Mailgun API.

## Features

- Easy-to-use GUI dialog for collecting issue information from users
- Automatic system information collection
- Internationalization support
- Integration with Mailgun for sending emails

## Installation

You can install Issue Reporter using pip:

```
pip install issue-reporter
```

## Usage

The primary way to use Issue Reporter is through its GUI. Here's how to integrate it into your application:

```python
from issue_reporter.gui import IssueReporterDialog
from issue_reporter import IssueReporter
import wx

# Initialize the IssueReporter
reporter = IssueReporter(
    from_address='errors@yourdomain.com',
    to_address='support@yourdomain.com',
    mailgun_api_key='your-mailgun-api-key'
)

# Create and show the dialog
app = wx.App()
dialog = IssueReporterDialog(None)
if dialog.ShowModal() == wx.ID_OK:
    report = dialog.get_report()
    reporter.send_report(report)
dialog.Destroy()
app.MainLoop()
```

This code snippet will display a dialog box for the user to fill out the issue report. When the user clicks OK, the report is automatically sent using the configured IssueReporter.

## Configuration

The `IssueReporter` class requires the following parameters:

- `from_address`: The email address from which the reports will be sent
- `to_address`: The email address to which the reports will be sent
- `mailgun_api_key`: Your Mailgun API key

## Internationalization

Issue Reporter supports internationalization. The GUI automatically uses the appropriate translation based on the system's locale settings. Translations are available in several languages, including German, Spanish, French, and more.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for the full license text.

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.

---

Copyright (c) 2023 Christopher Toth
