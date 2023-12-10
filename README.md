# Daily Reminder Email Program

This Python script allows you to send a daily reminder email containing positive quotes or affirmations to a specified recipient. The program uses the SMTP protocol to connect to popular email service providers (Gmail, Yahoo, Outlook, AT&T, Comcast).

## How to Use

1. Run the script.
2. Choose an email service provider.
3. Enter your email address and **app-specific password** when prompted.
4. Select a recipient's email address.
5. The program will generate a daily reminder email with random positive quotes and send it.

## Getting App-Specific Passwords

### Gmail:

1. Go to your [Google Account Security](https://myaccount.google.com/security-checkup).
2. Under "Signing in to Google," click on "App passwords."
3. Sign in to your Google account if prompted.
4. Select "Mail" and "Other (Custom name)" for the app.
5. Click "Generate."
6. Use the generated app-specific password in the script.

### Yahoo:

1. Go to your [Yahoo Account Security](https://login.yahoo.com/account/security).
2. Under "App passwords," generate a new password.
3. Use the generated app-specific password in the script.

### Outlook:

1. Go to your [Microsoft Security](https://account.microsoft.com/security).
2. Under "Security basics," find "App passwords."
3. Generate a new app password and use it in the script.

### Other Providers:

For other email providers, check their security or account settings for options related to app passwords or third-party access.

**Remember to keep these app-specific passwords secure and do not share them openly. If you're unsure about generating an app-specific password, consult your email provider's documentation or support for specific instructions.**

## Dependencies

- Python 3.x
- smtplib module (standard library)
- random library
- time library

## Usage

```bash
python daily_reminder.py
