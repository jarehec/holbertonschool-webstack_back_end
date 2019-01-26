#!/usr/bin/python3
"""
user session module
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String


class UserSession(BaseModel, Base):
    """ session database table """
    user_id = Column(String(60), nullable=False)
    session_id = Column(String(60), nullable=False)
    __tablename__ = 'user_sessions'
