#!/usr/bin/python3

"""
module containing User class
"""
import hashlib
from models.base_model import BaseModel


class User(BaseModel):
    """ user model """
    email = None
    first_name = None
    last_name = None
    _password = None

    def display_name(self):
        """ displays user info """
        if self.email == self.first_name == self.last_name is None:
            return ''
        elif self.email is not None and (self.first_name ==
                                         self.last_name is None):
            return self.email
        elif self.first_name is not None and self.last_name is None:
            return self.first_name
        elif self.last_name is not None and self.first_name is None:
            return self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    def __str__(self):
        """ return string representation of user """
        return '[{}] {} - {} - {}'.format(self.__class__.__name__,
                                          self.id, self.email,
                                          self.display_name())

    def is_valid_password(self, pwd):
        """ checks if the password is valid """
        if type(pwd) is not str or self._password is None:
            return False
        pwd = hashlib.md5(bytes(pwd, encoding='utf8')).hexdigest()
        return pwd == self._password
        

    @property
    def password(self):
        """ getter for pasword attribute """
        return self._password

    @password.setter
    def password(self, value):
        """ setter for password """
        if value is None or type(value) is not str:
            self._password = None
        else:
            value = hashlib.md5(bytes(value, encoding='utf8')).hexdigest()
            self._password = value
