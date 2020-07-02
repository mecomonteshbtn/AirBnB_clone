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
from models.review import Review


class TestReview(unittest.TestCase):
    """
    class for testing Review class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_Review(self):
        """
        Test that review.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Review(self):
        """
        Test that test_review.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        self.R = Review()

    def tearDown(self):
        self.R = None

    def test_type(self):
        """test method for type testing of review
        """
        self.assertIsInstance(self.R, Review)
        self.assertEqual(type(self.R), Review)
        self.assertEqual(issubclass(self.R.__class__, Review), True)
        self.assertEqual(isinstance(self.R, Review), True)

    def test_place_id_type(self):
        """tests the place_id class attribute type of Review
        """
        self.assertEqual(type(Review.place_id), str)

    def test_user_id_type(self):
        """tests the user_id class attribute type of Review
        """
        self.assertEqual(type(Review.user_id), str)

    def test_text_type(self):
        """tests the text class attribute type of Review
        """
        self.assertEqual(type(Review.text), str)

    def test_string_return(self):
        """tests the string method
        """
        string = str(self.R)
        Rid = "[{}] ({})".format(self.R.__class__.__name__,
                                 self.R.id)
        test = Rid in string
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
        my_dict = self.R.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.R.created_at.isoformat())
        self.assertEqual(datetime, type(self.R.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.R.__class__.__name__)
        self.assertEqual(my_dict['id'], self.R.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.R.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.R.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.R.to_dict()
        R1 = self.R.__class__(**my_dict)
        self.assertEqual(R1.id, self.R.id)
        self.assertEqual(R1.updated_at, self.R.updated_at)
        self.assertEqual(R1.created_at, self.R.created_at)
        self.assertEqual(R1.__class__.__name__,
                         self.R.__class__.__name__)

    def test_from_dict_hard(self):
        """test from_dict method for class objects
        """
        self.R.name = 'Meco'
        my_dict = self.R.to_dict()
        self.assertEqual(my_dict['name'], 'Meco')
        R1 = self.R.__class__(**my_dict)
        self.assertEqual(R1.created_at, self.R.created_at)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        R1 = self.R.__class__()
        R2 = self.R.__class__()
        self.assertNotEqual(self.R.id, R1.id)
        self.assertNotEqual(self.R.id, R2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.R.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.R.updated_at
        self.R.save()
        time2 = self.R.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
