#!/usr/bin/python3
"""
module containing Auth class
"""
from flask import request


class Auth():
    """ authentication class """
    def require_auth(self, path, excluded_paths):
        """ checks if a route requires authentication """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        path = path + '/' if path[-1] != '/' else path
        return path not in excluded_paths

    def authorization_header(self, request=None):
        """ validates requests """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None):
        """ TODO """
        return None
