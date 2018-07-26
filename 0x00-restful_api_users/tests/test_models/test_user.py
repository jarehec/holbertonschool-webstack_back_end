#!/usr/bin/python3

from datetime import datetime
from models.user import User
import unittest
import uuid


class TestUserModel(unittest.TestCase):
    """ tests for base model class """
    def setUp(self):
        """ test setup """
        self.user = User()

    def test_model(self):
        """ test user instance """
        self.assertIsNotNone(self.user)
        self.assertIsInstance(self.user, User)

    def test_id(self):
        """ test user id """
        self.assertEqual(self.user.id, str(uuid.UUID(self.user.id, version=4)))
        self.assertIsNotNone(self.user.id)
        self.assertIsInstance(self.user.id, str)

    def test_created_at(self):
        """ test user created_at """
        self.assertIsNotNone(self.user.created_at)
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at(self):
        """ test user updated_at """
        self.assertIsNotNone(self.user.updated_at)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_display_name_all_none(self):
        """ test with email, first_name, last_name as None """
        print(self.user.display_name()), "benis"
        self.assertEqual(self.user.display_name(), '')

    def test_display_name_email(self):
        """ test with first_name, last_name as None """
        self.user.email = 'james@bond.com'
        self.assertEqual(self.user.display_name(), 'james@bond.com')

    def test_display_name_first_name(self):
        """ test with email, last_name as None """
        self.user.first_name = 'james'
        self.assertEqual(self.user.display_name(), 'james')

    def test_display_name_last_name(self):
        """ test with email, last_name as None """
        self.user.last_name = 'bond'
        self.assertEqual(self.user.display_name(), 'bond')

    def test_display_name_email_first_name(self):
        """ test with last_name as None """
        self.user.first_name = 'james'
        self.user.email = 'james@bond.com'
        self.assertEqual(self.user.display_name(), 'james')

    def test_display_name_email_last_name(self):
        """ test with first_name as None """
        self.user.last_name = 'bond'
        self.user.email = 'james@bond.com'
        self.assertEqual(self.user.display_name(), 'bond')

    def test_display_name_all_filled(self):
        """ test with email, first_name, last_name not None """
        self.user.first_name = 'james'
        self.user.last_name = 'bond'
        self.user.email = 'james@bond.com'
        self.assertEqual(self.user.display_name(), 'james bond')

    def test_str_email(self):
        """ test with email not None """
        self.user.email = 'james@bond.com'
        self.assertEqual(str(self.user), '[User] ' + self.user.id +
                         ' - james@bond.com - james@bond.com')

    def test_str_first_name(self):
        """ test with first_name not None """
        self.user.first_name = 'james'
        self.assertEqual(str(self.user), '[User] ' + self.user.id +
                         ' - None - james')

    def test_str_last_name(self):
        """ test with last_name not None """
        self.user.last_name = 'bond'
        self.assertEqual(str(self.user), '[User] ' + self.user.id +
                         ' - None - bond')

    def test_str_all_filled(self):
        """ test with email, first_name, last_name not None """
        self.user.first_name = 'james'
        self.user.last_name = 'bond'
        self.user.email = 'james@bond.com'
        self.assertEqual(str(self.user), '[User] ' + self.user.id +
                         ' - james@bond.com - james bond')

    def test_password_none(self):
        """ test when password is None """
        self.assertEqual(self.user.password, None)

    def test_password_str(self):
        """ test password """
        self.user.password = 'Bogdanoff'
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password,
                         '425e87e2c815b85d5649d663d4ccc4de')

    def test_is_valid_password(self):
        """ test is_valid_password """
        self.assertFalse(self.user.is_valid_password('bogdanoff'))
        self.assertFalse(self.user.is_valid_password(None))
        self.user.password = 'Bogdanoff'
        self.assertTrue(self.user.is_valid_password('Bogdanoff'))
        self.assertFalse(self.user.is_valid_password(98))
        self.assertFalse(self.user.is_valid_password({'pass': 'word'}))

    def test_to_dict(self):
        """ test to_dict() method """
        test_emails = ["hbtn@hbtn.com", 3, True, None, {'e': 1}, (2,)]
        test_names = ["Bob", 15, None, True, {False: True}, (31,)]
        test_lastnames = ["Ross", 15, None, True, {False: True}, (12,)]
        for i in range(len(test_emails)):
            self.user.email = test_emails[i]
            self.user.first_name = test_names[i]
            self.user.last_name = test_lastnames[i]
            d = self.user.to_dict()
            for key, val in d.items():
                self.assertIsInstance(val, str)
                self.assertIsNotNone(val)

    def test_to_dict_date(self):
        """ test that dates are formatted correctly """
        d = self.user.to_dict()
        test_date = [d['updated_at'], d['created_at']]
        self.assertIsNotNone(test_date[0])
        self.assertIsNotNone(test_date[1])
        self.assertIsInstance(test_date[0], str)
        self.assertIsInstance(test_date[1], str)
        self.assertIsInstance(datetime.strptime(test_date[0],
                              '%Y-%m-%d %H:%M:%S'), datetime)
        self.assertIsInstance(datetime.strptime(test_date[1],
                              '%Y-%m-%d %H:%M:%S'), datetime)

if __name__ == '__main__':
    unittest.main()
