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

def send_email():
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_email()