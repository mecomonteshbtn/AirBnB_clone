#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:28:17 2020

@author: Robinson Montes
         Carlos Murcia
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel

    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """init method for User class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
