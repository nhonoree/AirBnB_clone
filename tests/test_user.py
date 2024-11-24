#!/usr/bin/python3
"""Test suite for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up resources for testing."""
        self.user = User()

    def test_instance_creation(self):
        """Test if object is correctly created."""
        self.assertIsInstance(self.user, User)


if __name__ == '__main__':
    unittest.main()
