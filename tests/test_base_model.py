#!/usr/bin/python3
"""Test suite for the BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up resources for testing."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if object is correctly created."""
        self.assertIsInstance(self.model, BaseModel)

    def test_attributes(self):
        """Test if attributes are set correctly."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
