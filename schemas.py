from pydantic import BaseModel
from typing import Optional


class Validation(BaseModel):
    number: str


class Instagram(BaseModel):
    url: str


# class ShowPost(PostModel):
#     class Config:
#         orm_mode = True
