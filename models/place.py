#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:28:17 2020

@author: Robinson Montes
         Carlos Murcia
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inherits from BaseModel

    Attributes:
        city_id (str): Public class attribute for Place's city_id
        user_id (str): Public class attribute for Place's user_id
        name (str): Public class attribute for Place's name
        description (str): Public class attribute for Place's description
        number_rooms (int): Public class attribute for Place's number_rooms
        number_bathrooms (int): Public class attribute for Place's
            number_bathrooms
        max_guest (str): Public class attribute for Place's max_guest
        price_by_night (str): Public class attribute for Place's price_by_night
        latitude (float): Public class attribute for Place's latitude
        longitude (float): Public class attribute for Place's longitude
        amenity_ids (list): Public class attribute for Place's amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """init method for Place class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
