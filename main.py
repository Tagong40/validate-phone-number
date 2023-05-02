from typing import Union
from schemas import Validation, IpAddress, Generate
from fastapi import FastAPI, HTTPException, Response, Header, Depends
from validate import validate
import socket
from ip import get_ip
import secrets
from database import engine, SessionLocal
from models import Base, User
from sqlalchemy.orm import Session
from mail import send_email


REMOTE_SERVER = "www.google.com"

Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def version():
    return {"version": "1.0.0"}


@app.post("/generate-key")
async def generate_key(request: Generate, db: Session = Depends(get_db)):
    api_key = secrets.token_hex(20)
    new_user = User(email=request.email, key=api_key,
                    re_key=secrets.token_hex(4).upper())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    send_email(request.email, api_key)
    return {"message": "check your email for api_key!!"}


@app.post("/check/phone_number")
def validate_number(request: Validation, db: Session = Depends(get_db), api_key: str = Header(...)):
    key_exists = db.query(User).filter(User.key == api_key).first()

    if not key_exists:
        raise HTTPException(status_code=400, detail="Invalid API key")
    return validate(request.number)


@app.get("/detect/online")
def online(api_key: str = Header(...), db: Session = Depends(get_db)):
    key_exists = db.query(User).filter(User.key == api_key).first()

    if not key_exists:
        raise HTTPException(status_code=400, detail="Invalid API key")

    try:
        socket.create_connection((REMOTE_SERVER, 80))
        return {'online': True}
    except OSError:
        return {'online': False}


@app.post("/ip/verify")
def verifyIp(request: IpAddress, db: Session = Depends(get_db), api_key: str = Header(...)):
    key_exists = db.query(User).filter(User.key == api_key).first()

    if not key_exists:
        raise HTTPException(status_code=400, detail="Invalid API key")

    return get_ip(request.ip)
