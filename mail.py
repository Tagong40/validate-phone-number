import smtplib
from email.mime.text import MIMEText
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def send_email(recipient, message):

    email = MIMEText(message)
    email['To'] = recipient
    email['From'] = "api@tensangna.online"
    email['Subject'] = "Your Api Key"

    server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
    # server.starttls()
    server.login("api@tensangna.online", "@Tagone20")

    try:
        server.sendmail("Tensangna@tensangna.online",
                        recipient, email.as_string())

    except Exception as e:
        response = {"message": str(e)}
        status_code = 500

        return response
