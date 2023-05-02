from pydantic import BaseModel
from typing import Optional


class Validation(BaseModel):
    number: str


class Generate(BaseModel):
    email: str


class IpAddress(BaseModel):
    ip: str


# class ShowPost(PostModel):
#     class Config:
#         orm_mode = True
