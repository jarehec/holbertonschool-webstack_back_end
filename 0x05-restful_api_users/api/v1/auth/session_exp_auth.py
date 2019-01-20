#!/usr/bin/python3
"""
module containing SessionExpAuth class
"""
import os
import uuid
from .auth import Auth
from datetime import datetime, timedelta
from models import db_session
from models.user import User

class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class """
    def __init__(self):
        try:
            session_duration = int(os.getenv('HBNB_YELP_SESSION_DURATION'))
        except:
            session_duration = 0

    def create_session(self, user_id=None):
        sess_id = super().create_session()
        if sess_id is None:
            return None
        self.user_id_by_session_id[sess_id] = {
                                                'user_id': user_id,
                                                'created_at': datetime.now()
                                              }
        return sess_id

    def user_id_for_session_id(self, session_id=None):
        if session_id is None:
            return None
        if self.user_id_by_session_id.get(session_id) is None:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        if self.user_id_by_session_id[session_id].get('created_at') is None:
            return None
        if timedelta(self.session_duration) + timedelta(
