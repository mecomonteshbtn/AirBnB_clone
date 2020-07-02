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
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    class for testing Place class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_Place(self):
        """
        Test that place.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """
        Test that test_place.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up method for place class
        """
        self.P = Place()

    def tearDown(self):
        """initialized method for place
        """
        self.P = None

    def test_type(self):
        """test method for type testing of place
        """
        self.assertIsInstance(self.P, Place)
        self.assertEqual(type(self.P), Place)
        self.assertEqual(issubclass(self.P.__class__, Place), True)
        self.assertEqual(isinstance(self.P, Place), True)

    def test_city_id_type(self):
        """tests the city_id class attributes type for Place
        """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id_type(self):
        """tests the user_id class attributes type for Place
        """
        self.assertEqual(type(Place.user_id), str)

    def test_name_type(self):
        """tests the name class attributes type for Place
        """
        self.assertEqual(type(Place.name), str)

    def test_description_type(self):
        """tests the description class attributes type for Place
        """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms_type(self):
        """tests the number_rooms class attributes type for Place
        """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms_type(self):
        """tests the number_bathrooms class attributes type for Place
        """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest_type(self):
        """tests the max_guest class attributes type for Place
        """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night_type(self):
        """tests the price_by_night class attributes type for Place
        """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude_type(self):
        """tests the latitude class attributes type for Place
        """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude_type(self):
        """tests the longitude class attributes type for Place
        """
        self.assertEqual(type(Place.longitude), float)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.P.first_name = 'Meco'
        self.P.last_name = 'Montes'
        self.assertEqual(self.P.first_name, 'Meco')
        self.assertEqual(self.P.last_name, 'Montes')

    def test_string_return(self):
        """tests the string method
        """
        string = str(self.P)
        Pid = "[{}] ({})".format(self.P.__class__.__name__,
                                 self.P.id)
        test = Pid in string
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
        my_dict = self.P.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.P.created_at.isoformat())
        self.assertEqual(datetime, type(self.P.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.P.__class__.__name__)
        self.assertEqual(my_dict['id'], self.P.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.P.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.P.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.P.to_dict()
        P1 = self.P.__class__(**my_dict)
        self.assertEqual(P1.id, self.P.id)
        self.assertEqual(P1.updated_at, self.P.updated_at)
        self.assertEqual(P1.created_at, self.P.created_at)
        self.assertEqual(P1.__class__.__name__,
                         self.P.__class__.__name__)

    def test_from_dict_hard(self):
        """test from_dict method for class objects
        """
        self.P.name = 'Meco'
        self.P.amenity_ids = ['90870987907', '0897909', '987907']
        my_dict = self.P.to_dict()
        self.assertEqual(my_dict['name'], 'Meco')
        P1 = self.P.__class__(**my_dict)
        self.assertEqual(P1.created_at, self.P.created_at)
        self.assertEqual(type(P1.number_rooms), int)
        self.assertEqual(type(P1.number_bathrooms), int)
        self.assertEqual(type(P1.max_guest), int)
        self.assertEqual(type(P1.price_by_night), int)
        self.assertEqual(type(P1.latitude), float)
        self.assertEqual(type(P1.longitude), float)
        self.assertEqual(type(P1.amenity_ids), list)
        self.assertEqual(self.P.number_rooms, P1.number_rooms)
        self.assertEqual(self.P.number_bathrooms,
                         P1.number_bathrooms)
        self.assertEqual(self.P.max_guest, P1.max_guest)
        self.assertEqual(self.P.price_by_night, P1.price_by_night)
        self.assertEqual(self.P.latitude, P1.latitude)
        self.assertEqual(self.P.longitude, P1.longitude)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        P1 = self.P.__class__()
        P2 = self.P.__class__()
        self.assertNotEqual(self.P.id, P1.id)
        self.assertNotEqual(self.P.id, P2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.P.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.P.updated_at
        self.P.save()
        time2 = self.P.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
