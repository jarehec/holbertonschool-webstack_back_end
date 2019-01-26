#!/usr/bin/python3
"""
session database authentication
"""
import uuid
from .session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models import db_session
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ database sessions class """
    def create_session(self, user_id=None):
        """ overloaded create_session method """
        sess_id = super().create_session(user_id)
        if sess_id is None:
            return None
        try:
            sess = UserSession()
            sess.user_id = user_id
            sess.session_id = sess_id
            db_session.add(sess)
            db_session.commit()
            return sess.session_id
        except:
            return None

    def user_id_for_session_id(self, session_id=None):
        """ returns a User id based on session id """
        if type(session_id) is not str:
            return None
        try:
            sess = db_session.query(UserSession).filter(
                                UserSession.session_id == session_id).one()
            if self.session_duration <= 0:
                return sess.user_id
            if timedelta(seconds=self.session_duration) + \
               self.user_id_by_session_id[session_id]['created_at'] < \
               datetime.now():
                return None

            return sess.user_id
        except:
            return None

    def destroy_session(self, request=None):
        """ removes a session """
        try:
            sess_id = self.session_cookie(request)
            if sess_id is None:
                return False

            sess = db_session.query(UserSession).filter(
                                UserSession.session_id == sess_id).one()
            db_session.delete(sess)
            db_session.commit()
            return True
        except:
            return False
