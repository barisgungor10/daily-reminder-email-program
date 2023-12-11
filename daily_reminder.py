# Importing necessary modules for the daily reminder script
import requests  # For making HTTP requests
import bs4  # For parsing HTML and extracting information
import random  # For randomly selecting quotes
import smtplib  # For sending emails using SMTP
import time  # For measuring the execution time of the script
from quotes import quotes_list  # For quotes from the list

# Record the starting time of the program execution
starting_time = time.time()

# Operations available for the user
operations = ('motivational quotes', 'horoscope quotes')
decision = ''

# Variables for horoscope feature
horoscope = ''
horoscope_list = ('gemini', 'libra', 'taurus', 'scorpio', 'aries', 'pisces', 'aquarius', 'leo', 'cancer', 'sagittarius',
                  'capricorn')
horoscope_date = ''
horoscope_quote = ''

# Variables for email functionality
mail_addresses = ('gmail', 'yahoo', 'outlook', 'at&t', 'comcast')
mail_address = ''
mail_bool = False
login_bool = False
subject = 'DAILY REMINDER'
body = ''
message = ''

# Choosing an email service provider
while not mail_bool:
    mail_address = input('Which mail do you want to use? (gmail/yahoo/outlook/at&t/comcast): ')

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
        password = input('Enter your application key: ')
        smtp_object.login(user, password)
        break
    except smtplib.SMTPAuthenticationError:
        print('You entered wrong information! Please try again.')

# Specifying the recipient's email address
to_mail = input('Who do you want to send the message?: ')

while decision not in operations:
    decision = input('Which operation do you want to do? (horoscope quotes/motivational quotes): ').lower()
    if decision not in operations:
        print('You entered an invalid operation. Please try again!')
    else:
        break

if decision == operations[0]:
    for quotes in random.sample(quotes_list, k=5):
        body += f'{quotes}\n'

    # Constructing the email message for motivational quotes
    message = f'Subject: DAILY REMINDER\n{body}'

elif decision == operations[1]:
    while horoscope not in horoscope_list:
        horoscope = input('Which horoscope do you want to search for?: ').lower()
        if horoscope not in horoscope_list:
            print('You entered the wrong input!')
        else:
            break

    # Fetching horoscope information from the web
    website_link = requests.get(f"https://www.washingtonpost.com/entertainment/horoscopes/{horoscope}/")
    organized_website_link = bs4.BeautifulSoup(website_link.text, "html.parser")

    horoscope_date = organized_website_link.select('.w-100 .b.pa-sm .light.gray-dark.font-md.pl-sm')[0].text
    horoscope_quote = organized_website_link.select('.w-100 .b.pa-sm .mt-sm.mb-sm.font-sm.gray-dark')[0].text

    # Constructing the email message for horoscope quotes
    message = f'Subject: HOROSCOPE REPORT\n{horoscope.upper()}\t{horoscope_date}\n{horoscope_quote}'

# Sending the email
smtp_object.sendmail(mail_address, to_mail, message)

# Quitting the SMTP connection
smtp_object.quit()

# Calculating and displaying the program's execution time
ending_time = time.time()
print(f'The program has an execution time of: {ending_time - starting_time} seconds')
