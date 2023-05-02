import smtplib
from email.mime.text import MIMEText
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def send_email(recipient, message):

    # Set up email message
    email = MIMEText(message)
    email['To'] = recipient
    email['From'] = "hogarghana@gmail.com"
    email['Subject'] = "Free Api Token"

    # Set up SMTP server connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("hogarghana@gmail.com", "nnlutblemheymfsr")

    # Send email
    try:
        server.sendmail("hogarghana@gmail.com", recipient, email.as_string())
        response = {"message": "check your email for your token!!"}
        status_code = 200
    except Exception as e:
        response = {"message": str(e)}
        status_code = 500

    server.quit()

    # return JSONResponse(content=response, status_code=status_code)
