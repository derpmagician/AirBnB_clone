#!/usr/bin/python3
"""
File storage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class FileStorage:
    """ class that store information of the BaseModel Class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method that returns all objects """
        return self.__objects

    def new(self, obj):
        """ method that adds a new object """
         self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ method that saves a new object """
        new = {}
        for elem in self.__objects:
            new[elem] = self.__objects[elem].to_dict()
        with open(self.__file_path, 'w') as fd:
            json.dump(new, fd)

    def reload(self):
        """ method that loads the objectos from de file """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as fd:
                var = json.load(fd)
                for elem in var:
                    aux = classes[var[elem]['__class__']]
                    self.__objects[elem] = aux(**(var[elem]))
