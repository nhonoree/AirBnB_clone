#!/usr/bin/python3
"""Test suite for the FileStorage class."""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up resources for testing."""
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_all(self):
        """Test the all method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
