# Daily Reminder Script

## Table of Contents
1. Overview
2. Features
3. Configuration
4. How to Use
5. How to Get Application Password for Gmail
6. Execution Time

## Overview <a name="overview"></a>

This script is designed to send daily reminders to the user via email. The reminders can be either motivational quotes or horoscope quotes. The script uses the SMTP protocol to send emails and supports multiple email service providers.

## Features <a name="features"></a>

### Motivational Quotes

If the user chooses this feature, the script will randomly select five quotes from a predefined list in the `quotes` module. These quotes are then sent as a daily reminder to the recipient's email address.

### Horoscope Quotes

If the user chooses this feature, they will be prompted to enter a zodiac sign. The script will then fetch the daily horoscope for the specified zodiac sign from the web and send it as a daily reminder to the recipient's email address.

### Email Functionality

The script uses the SMTP protocol to send emails. It supports multiple email service providers including Gmail, Yahoo, Outlook, AT&T, and Comcast. The user will be prompted to enter their email address and application key to log in to their email account. They will also need to specify the recipient's email address.

## Configuration <a name="configuration"></a>

Before running the script, the user needs to provide some configuration:

- **Email Service Provider**: The user will be prompted to specify their email service provider. The script currently supports Gmail, Yahoo, Outlook, AT&T, and Comcast.
- **Email Account**: The user will be prompted to enter their email address and application key to log in to their email account.
- **Recipient's Email Address**: The user will be prompted to specify the recipient's email address.
- **Operation**: The user will be prompted to choose between motivational quotes and horoscope quotes.

## How to Use <a name="how-to-use"></a>

1. Run the script.
2. When prompted, choose an email service provider (gmail/yahoo/outlook/at&t/comcast).
3. Enter your email address and application key to log in to your email account.
4. Specify the recipient's email address.
5. Choose the operation you want to do (horoscope quotes/motivational quotes).
6. If you choose horoscope quotes, enter the horoscope you want to search for.
7. The script will send an email with the chosen type of quote to the specified recipient.

## How to Get Application Password for Gmail <a name="how-to-get-application-password-for-gmail"></a>

1. Go to your [Google Account Security](https://myaccount.google.com/security-checkup).
2. Under "Signing in to Google," click on "App passwords."
3. Sign in to your Google account if prompted.
4. Select "Mail" and "Other (Custom name)" for the app.
5. Click "Generate."
6. Use the generated app-specific password in the script.

## How to Get Application Password for Yahoo <a name="how-to-get-application-password-for-yahoo"></a>

1. Go to your [Yahoo Account Security](https://login.yahoo.com/account/security).
2. Under "App passwords," generate a new password.
3. Use the generated app-specific password in the script.

## How to Get Application Password for Outlook <a name="how-to-get-application-password-for-outlook"></a>

1. Go to your [Microsoft Security](https://account.microsoft.com/security).
2. Under "Security basics," find "App passwords."
3. Generate a new app password and use it in the script.

**Note**: Most of the time, you’ll only have to enter an App Password once per app or device, so don’t worry about memorizing it.

## Execution Time <a name="execution-time"></a>

At the end of its execution, the script calculates and displays the time it took to run. This can be useful for performance monitoring and optimization.
