from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users_py'

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    re_key = Column(String)
    email = Column(String)
