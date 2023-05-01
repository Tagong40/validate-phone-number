from typing import Union
from schemas import Validation, Instagram
from fastapi import FastAPI
from phoneValidate import validate
import socket
from ipAddress import ip

REMOTE_SERVER = "www.google.com"

app = FastAPI()


@app.post("/check/phone_number")
def validate_number(request: Validation):
    return validate(request.number)


@app.get("/detect/online")
def online():
    try:
        socket.create_connection((REMOTE_SERVER, 80))
        return {'online': True}
    except OSError:
        return {'online': False}


@app.post("/ip/verify")
def instaDownloader(request: Instagram):
    ip('8.8.8.8')
    return request
