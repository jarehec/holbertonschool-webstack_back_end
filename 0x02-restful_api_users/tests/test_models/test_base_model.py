#!/usr/bin/python3

from datetime import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """ tests for base model class """
    def setUp(self):
        """ test setup """
        self.model = BaseModel()

    def test_model(self):
        """ test model object """
        self.assertIsNotNone(self.model)
        self.assertIsInstance(self.model, BaseModel)

    def test_id(self):
        """ test model id """
        self.assertEqual(self.model.id,
                         str(uuid.UUID(self.model.id, version=4)))
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """ test model created_at """
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """ test model updated_at """
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
