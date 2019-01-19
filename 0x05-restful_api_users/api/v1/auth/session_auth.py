#!/usr/bin/python3
"""
module containing SessionAuth class
"""
import uuid
from .auth import Auth
from models import db_session
from models.user import User


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

    def user_id_for_session_id(self, session_id=None):
        """ returns a User id based on session id """
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value """
        try:
            cookie = self.session_cookie(request)
            uid = self.user_id_for_session_id(cookie)
            user = db_session.query(User).filter(User.id == uid).one()
            return user
        except:
            return None

    def destroy_session(self, request=None):
        """ removes a session """
        try:
            sess_id = self.session_cookie(request)
            print(sess_id)
            if sess_id is None:
                return False

            uid = self.user_id_for_session_id(sess_id)
            print(uid)
            if uid is None:
                return False
            del self.user_id_by_session_id[sess_id]
            return True
        except:
            return False
