#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:28:17 2020

@author: Robinson Montes
         Carlos Murcia
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel

    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method for Review class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
