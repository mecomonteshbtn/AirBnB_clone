#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
base_model that defines all common attributes/methods for other classes
Creation date: June 26, 2020
Authors: Robinson Montes, Carlos Murcia
"""
import uuid
import datetime

class BaseModel():
	"""
	base_model that defines all common attributes/methods for other classes
	"""
	def __init__(self):
		"""init method for BaseModel Class

		Args:
		    id : string - assign with an uuid when an instance is created
		    created_at : datetime - assign with the current datetime when an instance is created
		    updated_at : datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
	
	def __str__(self):
		"""str method for BaseModel Class

		Returns:
		    string (str): string descriptor for BaseModel Class
		"""
		string = "[" + str(self.__class__.__name__) + "] ("
		string += str(self.id) + ") " + str(self.__dict__)
		return string
	
	def save(self):
		"""
		updates the public instance attribute updated_at with the current datetime
		"""
		self.updated_at = datetime.datetime.now()
	def to_dict(self):
		"""returns a dictionary containing all keys/values of __dict__ of the instance:

		Returns:
		[dict]: [dictionary]
		"""
		dictionary = self.__dict__.copy()
		dictionary["created_at"] = self.created_at.isoformat()
		dictionary["updated_at"] = self.updated_at.isoformat()
		dictionary["__class__"] = self.__class__.__name__
		return dictionary
