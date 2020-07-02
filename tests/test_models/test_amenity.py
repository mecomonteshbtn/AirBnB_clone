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
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    class for testing Amenity class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_Amenity(self):
        """
        Test that amenity.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Amenity(self):
        """
        Test that test_amenity.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_amenity.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """Set up method for amenity class
        """
        self.A = Amenity()

    def tearDown(self):
        """Initialized method for class Amenity
        """
        self.A = None

    def test_type(self):
        """test method for type testing of amenity
        """
        self.assertIsInstance(self.A, Amenity)
        self.assertEqual(type(self.A), Amenity)
        self.assertEqual(issubclass(self.A.__class__, Amenity), True)
        self.assertEqual(isinstance(self.A, Amenity), True)

    def test_name_type(self):
        """tests the name type of attribute
        """
        self.assertEqual(type(Amenity.name), str)

    def test_string_return(self):
        """tests the str method
        """
        string = str(self.A)
        Aid = "[{}] ({})".format(self.A.__class__.__name__,
                                 self.A.id)
        test = Aid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.A.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.A.created_at.isoformat())
        self.assertEqual(datetime, type(self.A.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.A.__class__.__name__)
        self.assertEqual(my_dict['id'], self.A.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.A.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.A.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.A.to_dict()
        A1 = self.A.__class__(**my_dict)
        self.assertEqual(A1.id, self.A.id)
        self.assertEqual(A1.updated_at, self.A.updated_at)
        self.assertEqual(A1.created_at, self.A.created_at)
        self.assertEqual(A1.__class__.__name__,
                         self.A.__class__.__name__)

    def test_from_dict_hard(self):
        """test for the from_dict method for class objects
        """
        my_dict = self.A.to_dict()
        A1 = self.A.__class__(**my_dict)
        self.assertEqual(A1.created_at, self.A.created_at)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        A1 = self.A.__class__()
        A2 = self.A.__class__()
        self.assertNotEqual(self.A.id, A1.id)
        self.assertNotEqual(self.A.id, A2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.A.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.A.updated_at
        self.A.save()
        time2 = self.A.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
