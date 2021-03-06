# This program sends an email with the ip address and current time.
# It is used to send an email every time the raspberry pi starts up.

import os
import smtplib
import subprocess

from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load the environment file for environment variable.
load_dotenv("./.env")

# Load the raspberry pi's email address, password, and the email to send the message to.
email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
email_to_send_to = os.getenv("SEND_TO")

# Get the ip address of the raspberry pi.
ip_config = subprocess.getoutput(["ifconfig", "wlan0"])

subject = "Raspberry Pi Start Report"
message = "Raspberry Pi Start Report\n" \
          "IP Config :: \n%s\n" % ip_config

# Connect to the gmail server and login.
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(email_address, password)

# Create the email to be sent.
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_to_send_to
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)
