#!/usr/bin/python3
"""
module containing the base model class
"""
import uuid
from datetime import datetime


class BaseModel:
    """ parent model for all future models """
    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        """ initializing """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
