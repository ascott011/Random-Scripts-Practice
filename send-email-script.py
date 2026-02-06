# send email script

import smtplib
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

