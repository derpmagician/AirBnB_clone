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

    def do_count(self, args):
        """count # of instances of a class"""
        if not args:
            print('** class name missing **')
        else:
            m = []
            objects = models.storage.all()
            data = args.split()
            if not data[0]:
                print("** class name missing **")
            elif data[0] not in classes:
                print("** class doesn't exist **")
            else:
                for i in objects:
                    if i.startswith(data[0]):
                        m = [i]
                print(len(m))

    def emptyline(self):
        """Ignore empty lines"""
        pass

    def do_quit(self, args):
        """Quit command to exit"""
        return True

    def do_EOF(self, args):
        """Quit command to exit at end of file"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
