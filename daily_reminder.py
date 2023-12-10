# Importing necessary modules for the daily reminder script
import random  # For randomly selecting quotes
import smtplib  # For sending emails using SMTP
import getpass  # For securely inputting the email account password
import time  # For measuring the execution time of the script
from quotes import quotes_list
# Record the starting time of the program execution
starting_time = time.time()

def daily_reminder():
    # Possible mail service providers
    mail_addresses = ('gmail', 'yahoo', 'outlook', 'at&t', 'comcast')
    mail_address = ''
    mail_bool = False
    login_bool = False
    subject = 'DAILY REMINDER'
    body = ''

    # Choosing an email service provider
    while not mail_bool:
        mail_address = input('Which mail do you want to use?(gmail/yahoo/outlook/at&t/comcast): ')

        # Validating the chosen email service provider
        for address in mail_addresses:
            if mail_address == address:
                mail_bool = True
        if not mail_bool:
            print('You entered the wrong mail!')

    # Connecting to the SMTP server
    smtp_object = smtplib.SMTP(f'smtp.{mail_address}.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()

    # Logging in to the email account
    while not login_bool:
        try:
            user = input('Enter your mail address: ')
            password = getpass.getpass('Enter your application key: ')
            smtp_object.login(user, password)
            break
        except smtplib.SMTPAuthenticationError:
            print('You entered wrong information! Please try again.')

    # Generating the body of the email with random quotes
    for quotes in random.sample(quotes_list, k=5):
        body += f'{quotes}\n'
    
    # Specifying the recipient's email address
    to_mail = input('Who do you want to send the message?: ')
    
    # Constructing the email message
    message = f'Subject: {subject}\n{body}'
    
    # Sending the email
    smtp_object.sendmail(mail_address, to_mail, message)
    
    # Quitting the SMTP connection
    smtp_object.quit()

# Executing the daily reminder function
daily_reminder()

# Calculating and displaying the program's execution time
ending_time = time.time()
print(f'The program has an execution time of: {ending_time - starting_time} seconds')
