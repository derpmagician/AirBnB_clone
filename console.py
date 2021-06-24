#!/usr/bin/python3
"""Console AirBnB"""
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import re
classes = {"BaseModel": BaseModel,
           "User": User,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Place": Place,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Class command interpreter."""

    prompt = "(hbnb) "

    def default(self, args):
        """No recognized command method"""
        data = args.split('.')
        if len(data) >= 2:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
