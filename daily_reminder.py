# Importing necessary modules for the daily reminder script
import random  # For randomly selecting quotes
import smtplib  # For sending emails using SMTP
import getpass  # For securely inputting the email account password
import time  # For measuring the execution time of the script

# Storing the starting time to calculate the execution time
starting_time = time.time()

# Predefined list of positive quotes or reminders
reminders = ("Start your day with gratitude.",
             "Take a deep breath, you've got this.",
             "Practice kindness, always.",
             "Set realistic goals for the day.",
             "Smile—it's contagious.",
             "Prioritize self-care.",
             "Focus on progress, not perfection.",
             "Drink water, stay hydrated.",
             "Embrace change with an open mind.",
             "Express your feelings, don't bottle them up.",
             "Learn something new today.",
             "Be present in the moment.",
             "Surround yourself with positivity.",
             "Find joy in the little things.",
             "Believe in your abilities.",
             "Take a break when needed.",
             "Connect with a friend or loved one.",
             "Organize your space for clarity.",
             "Challenge negative thoughts.",
             "Celebrate your achievements, big or small.",
             "Practice mindfulness.",
             "Listen more than you speak.",
             "Step outside your comfort zone.",
             "Accept imperfections, yours and others'.",
             "Laugh often—it's good for the soul.",
             "Stay curious and ask questions.",
             "Face challenges with resilience.",
             "Take a moment to appreciate nature.",
             "Practice active listening.",
             "Trust the process of life.",
             "Reflect on your day before sleep.",
             "Acknowledge and learn from mistakes.",
             "Practice patience with yourself and others.",
             "Keep a positive mindset.",
             "Be mindful of your energy.",
             "Exercise for a happy mind and body.",
             "Express gratitude for challenges—they build resilience.",
             "Practice deep breathing for relaxation.",
             "Choose happiness over perfection.",
             "Be your own biggest supporter.",
             "Disconnect from technology for a while.",
             "Believe in the power of your dreams.",
             "Celebrate the success of others.",
             "Face fears head-on.",
             "Learn to say no when necessary.",
             "Challenge negative self-talk.",
             "Plan for a restful night's sleep.",
             "Seek out inspiration daily.",
             "Be gentle with yourself on tough days.",
             "Learn to forgive, for your own peace.",
             "Practice random acts of kindness.",
             "Trust the timing of your life.",
             "Set boundaries on social media.",
             "Reflect on three things you're grateful for today.",
             "Focus on solutions, not problems.",
             "Take a digital detox.",
             "Make time for a hobby you enjoy.",
             "Let go of what you can't control.",
             "Face challenges with a positive attitude.",
             "Share your talents with the world.",
             "Connect with someone new today.",
             "Find joy in the simple pleasures.",
             "Visualize your goals coming to fruition.",
             "Be mindful of your thoughts—they shape your reality.",
             "Practice self-compassion.",
             "Learn from criticism without taking it personally.",
             "Surround yourself with uplifting people.",
             "Challenge yourself to learn from setbacks.",
             "Speak words of encouragement to yourself.",
             "Create a vision board for your dreams.",
             "Practice gratitude in challenging situations.",
             "Set aside time for self-reflection.",
             "Celebrate progress, no matter how small.",
             "Release the need for approval from others.",
             "Declutter your physical and mental space.",
             "Practice the art of letting go.",
             "Believe in your own worthiness.",
             "Express love to those around you.",
             "Trust the journey, even when it's uncertain.",
             "Take a break from multitasking.",
             "Appreciate the journey as much as the destination.",
             "Believe in the power of positive thinking.",
             "Face challenges with courage and strength.",
             "Express your creativity in some way.",
             "Practice self-discipline for personal growth.",
             "Trust yourself—you know more than you think.",
             "Make choices that align with your values.",
             "Focus on what you can control.",
             "Practice gratitude for your body and health.",
             "Be kind to yourself during times of stress.",
             "Reflect on how far you've come.",
             "Find joy in helping others.",
             "Face challenges as opportunities for growth.",
             "Express your needs and desires clearly.",
             "Learn to let go of perfectionism.",
             "Take time to appreciate the beauty around you.",
             "Embrace the power of saying 'no' when necessary.",
             "Believe in the potential for positive change.",
             "Choose love over fear in decision-making.",
             "Celebrate your uniqueness.",
             "Practice patience in all aspects of life.")


# Function to send a daily reminder email
def daily_reminder():
    # Supported email service providers
    mail_addresses = ('gmail', 'yahoo', 'outlook', 'at&t', 'comcast')
    
    # Initializing variables for email configuration
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
    for quotes in random.sample(reminders, k=5):
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
