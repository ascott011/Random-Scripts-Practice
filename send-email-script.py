# send email script

import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

# load environment variables from .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# create function to send email. Parameters when calling the function should include the email of the 
# recipient, the subject and the email body. These should be asked for when the script is run.
# the user can enter the email, subject and message when prompted. 

msg = EmailMessage()
msg['From'] = EMAIL
msg['To'] = input("Enter the recipient's email: ")
msg['Subject'] = input("Enter the subject of the email: ")
msg.set_content(input("Enter the message body of the email: "))

def send_email(to_email, subject, message):
    try:
        # connect to the SMTP server 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        # create the email
        email_message = f"Subject: {subject}\n\n{message}"

        # send the email
        server.sendmail(EMAIL, to_email, email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()