#Import Outlook library
import os
#Import Email message
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "practicepython@gmail.com" 
email_password = os.environ.get("PASSWORD")
email_receiver = "aaleshe2@gmail.com"

#Content of Email

subject = "Update Jira Tickets"
body = """
I've just made a commit to git hub
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())