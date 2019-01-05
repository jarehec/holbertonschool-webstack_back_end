#!/usr/bin/python3
"""
module containing SessionAuth class
"""
import uuid
from .auth import Auth

class SessionAuth(Auth):
    """ SessionAuth class """
    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        """ creates a Session ID for a user_id """
        if type(user_id) is not str:
            return None
        sess_id = str(uuid.uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id
