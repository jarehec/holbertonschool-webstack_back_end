#!/usr/bin/python3
"""
module containing BasicAuth class
"""
from .auth import Auth
from base64 import b64decode
from models import db_session
from models.user import User


class BasicAuth(Auth):
    """ basic auth class """
    def extract_base64_authorization_header(self, authorization_header):
        """ returns the base64 part of the authorization_header """
        if isinstance(authorization_header, str) is False:
            return None

        strs = authorization_header.split(' ')
        if strs[0] != 'Basic':
            return None

        return ' '.join(strs[1:])

    def decode_base64_authorization_header(self, base64_authorization_header):
        """ returns the decoded value of a base64 string """
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            return str(b64decode(base64_authorization_header),
                       encoding='utf-8')
        except:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """ returns the email and password of a base64 decoded string """
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        npc = decoded_base64_authorization_header.split(':')
        return npc[0], npc[1]

    def user_object_from_credentials(self, user_email, user_pwd):
        """ returns the User instance based on the email and pasword """
        if isinstance(user_email, str) is False:
            return None
        if isinstance(user_pwd, str) is False:
            return None

        try:
            usr = db_session.query(User).filter(User.email == user_email).one()
            if usr.is_valid_password(user_pwd) is False:
                return None
            return usr
        except:
            return None

    def current_user(self, request=None):
        """ basic user authentication """
        auth = self.authorization_header(request)
        auth = self.extract_base64_authorization_header(auth)
        auth = self.decode_base64_authorization_header(auth)
        email, pwd = self.extract_user_credentials(auth)
        return self.user_object_from_credentials(email, pwd)
