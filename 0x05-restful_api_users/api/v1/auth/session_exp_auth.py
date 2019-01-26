#!/usr/bin/python3
"""
module containing SessionExpAuth class
"""
import os
import uuid
from .session_auth import SessionAuth
from datetime import datetime, timedelta
from models import db_session
from models.user import User


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class """
    def __init__(self):
        """ SessionExpAuth constructor """
        try:
            self.session_duration = int(os.getenv(
                                        'HBNB_YELP_SESSION_DURATION'))
        except:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ overloaded create_session method """
        sess_id = super().create_session(user_id)
        if sess_id is None:
            return None
        self.user_id_by_session_id[sess_id] = {
                                                'user_id': user_id,
                                                'created_at': datetime.now()
                                              }
        return sess_id

    def user_id_for_session_id(self, session_id=None):
        """ overloaded user_id_by_session_id method """
        if session_id is None:
            return None
        if self.user_id_by_session_id.get(session_id) is None:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        if self.user_id_by_session_id[session_id].get('created_at') is None:
            return None
        if timedelta(seconds=self.session_duration) + \
           self.user_id_by_session_id[session_id]['created_at'] < \
           datetime.now():
            return None
        return self.user_id_by_session_id[session_id]['user_id']
