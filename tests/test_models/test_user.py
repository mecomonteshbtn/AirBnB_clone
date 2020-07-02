#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020
@author: meco
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.user import User


class TestUser(unittest.TestCase):
    """
    class for testing User class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_User(self):
        """
        Test that user.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """
        Test that test_user.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """Set up method for User class
        """
        self.Us = User()

    def tearDown(self):
        """Initialized User class
        """
        self.Us = None

    def test_type(self):
        """type checks for user model
        """
        self.assertEqual(issubclass(self.Us.__class__, User), True)
        self.assertEqual(isinstance(self.Us, User), True)
        self.assertEqual(isinstance(self.Us, User), True)
        self.assertEqual(type(self.Us), User)

    def test_basic_attribute_set(self):
        """Basic attribute tests for user model
        """
        self.Us.first_name = 'Meco'
        self.Us.last_name = 'Montes'
        self.assertEqual(self.Us.first_name, 'Meco')
        self.assertEqual(self.Us.last_name, 'Montes')

    def test_email(self):
        """tests the user's email attribute
        """
        self.assertEqual(type(User.email), str)

    def test_password(self):
        """tests the user's password attribute
        """
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        """tests the user's first_name attribute
        """
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """tests the user's last_name attribute
        """
        self.assertEqual(type(User.last_name), str)

    def test_string_return(self):
        """tests the str method
        """
        string = str(self.Us)
        Usid = "[User] ({})".format(self.Us.id)
        test = Usid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime.datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests the to_dict method
        """
        my_dict = self.Us.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.Us.created_at.isoformat())
        self.assertEqual(datetime, type(self.Us.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.Us.__class__.__name__)
        self.assertEqual(my_dict['id'], self.Us.id)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.Us.to_dict()
        Us1 = User(**my_dict)
        self.assertEqual(Us1.id, self.Us.id)
        self.assertEqual(Us1.updated_at, self.Us.updated_at)
        self.assertEqual(Us1.created_at, self.Us.created_at)
        self.assertEqual(Us1.__class__.__name__,
                         self.Us.__class__.__name__)

    def test_from_dict_hard(self):
        """tests from dict method of user inherited from base_model
        """
        self.Us.student = 'Science'
        my_dict = self.Us.to_dict()
        self.assertEqual(my_dict['student'], 'Science')
        Us1 = User(**my_dict)
        self.assertEqual(Us1.created_at, self.Us.created_at)
