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
from models.state import State


class TestState(unittest.TestCase):
    """
    class for testing State class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_State(self):
        """
        Test that state.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """
        Test that test_state.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up method for State class
        """
        self.S = State()

    def tearDown(self):
        """initialized method for State class
        """
        self.S = None

    def test_type(self):
        """test method for type testing of state
        """
        self.assertIsInstance(self.S, State)
        self.assertEqual(type(self.S), State)
        self.assertEqual(issubclass(self.S.__class__, State), True)
        self.assertEqual(isinstance(self.S, State), True)

    def test_name_type(self):
        """tests the type of state attribute
        """
        self.assertEqual(type(State.name), str)

    def test_string_return(self):
        """tests the string method
        """
        string = str(self.S)
        Sid = "[{}] ({})".format(self.S.__class__.__name__,
                                 self.S.id)
        test = Sid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime.datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.S.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.S.created_at.isoformat())
        self.assertEqual(datetime, type(self.S.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.S.__class__.__name__)
        self.assertEqual(my_dict['id'], self.S.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.S.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.S.created_at, time)

    def test_from_dict_basic(self):
        """tests from_dict method
        """
        my_dict = self.S.to_dict()
        S1 = self.S.__class__(**my_dict)
        self.assertEqual(S1.id, self.S.id)
        self.assertEqual(S1.updated_at, self.S.updated_at)
        self.assertEqual(S1.created_at, self.S.created_at)
        self.assertEqual(S1.__class__.__name__,
                         self.S.__class__.__name__)

    def test_from_dict_hard(self):
        """test from_dict method for class objects
        """
        self.S.name = 'Meco'
        my_dict = self.S.to_dict()
        self.assertEqual(my_dict['name'], 'Meco')
        S1 = self.S.__class__(**my_dict)
        self.assertEqual(S1.created_at, self.S.created_at)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        S1 = self.S.__class__()
        S2 = self.S.__class__()
        self.assertNotEqual(self.S.id, S1.id)
        self.assertNotEqual(self.S.id, S2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.S.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.S.updated_at
        self.S.save()
        time2 = self.S.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
