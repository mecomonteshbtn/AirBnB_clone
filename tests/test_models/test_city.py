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
from models.city import City


class TestCity(unittest.TestCase):
    """
    class for testing City class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_City(self):
        """
        Test that city.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_City(self):
        """
        Test that test_city.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """Set up mehtod for city class
        """
        self.C = City()

    def tearDown(self):
        """Initialized City class
        """
        self.C = None

    def test_type(self):
        """test method for type testing of city
        """
        self.assertIsInstance(self.C, City)
        self.assertEqual(type(self.C), City)
        self.assertEqual(issubclass(self.C.__class__, City), True)
        self.assertEqual(isinstance(self.C, City), True)

    def test_state_id_type(self):
        """tests the state_id type attribute
        """
        self.assertEqual(type(City.state_id), str)

    def test_name_type(self):
        """tests the name type of class attribute
        """
        self.assertEqual(type(City.name), str)

    def test_basic_attribute_set(self):
        """test method for basic attribute
        """
        self.C.first_name = 'Meco'
        self.C.last_name = 'Montes'
        self.assertEqual(self.C.first_name, 'Meco')
        self.assertEqual(self.C.last_name, 'Montes')

    def test_string_return(self):
        """tests the str method
        """
        string = str(self.C)
        Cid = "[{}] ({})".format(self.C.__class__.__name__,
                                 self.C.id)
        test = Cid in string
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
        my_dict = self.C.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.C.created_at.isoformat())
        self.assertEqual(datetime, type(self.C.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.C.__class__.__name__)
        self.assertEqual(my_dict['id'], self.C.id)

    def test_to_dict_more(self):
        """tests more things with to_dict method
        """
        my_dict = self.C.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.C.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.C.to_dict()
        C1 = self.C.__class__(**my_dict)
        self.assertEqual(C1.id, self.C.id)
        self.assertEqual(C1.updated_at, self.C.updated_at)
        self.assertEqual(C1.created_at, self.C.created_at)
        self.assertEqual(C1.__class__.__name__,
                         self.C.__class__.__name__)

    def test_from_dict_hard(self):
        """test for the from_dict method for class objects
        """
        self.C.first_name = 'Meco'
        self.C.last_name = 'Montes'
        my_dict = self.C.to_dict()
        self.assertEqual(my_dict['first_name'], 'Meco')
        C1 = self.C.__class__(**my_dict)
        self.assertEqual(C1.created_at, self.C.created_at)

    def test_unique_id(self):
        """test for unique ids in class objects
        """
        C1 = self.C.__class__()
        C2 = self.C.__class__()
        self.assertNotEqual(self.C.id, C1.id)
        self.assertNotEqual(self.C.id, C2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.C.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.C.updated_at
        self.C.save()
        time2 = self.C.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
