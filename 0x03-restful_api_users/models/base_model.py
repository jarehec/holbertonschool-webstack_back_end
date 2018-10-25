#!/usr/bin/python3
"""
module containing the base model class
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String

Base = declarative_base()


class BaseModel:
    """ parent model for all future models """
    id = Column(String(60), unique=True, nullable=False,
                default=str(uuid.uuid4()), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self):
        """ initializing """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
