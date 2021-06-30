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
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)

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
        """Ignores empty spaces"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program at end of file"""
        print()
        return True

    def do_create(self, args):
        """Creates an instance"""
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] not in classes:
                print("** class doesn't exist **")
            else:
                if s == "BaseModel":
                    obj = BaseModel()
                elif s == "User":
                    obj = User()
                elif s == "State":
                    obj = State()
                elif s == "City":
                    obj = City()
                elif s == "Amenity":
                    obj = Amenity()
                elif s == "Place":
                    obj = Place()
                else:
                    obj = Review()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        '''Print the object with id specified and his dictionary'''
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] not in classes:
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    if (data[0] + "." + data[1]) in all_objs:
                        print(storage.all()[data[0] + "." + data[1]])
                    else:
                        print("** no instance found **")

    def do_destroy(self, args):
        """ method that delete an object """
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] not in classes:
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    if (data[0] + "." + data[1]) in all_objs:
                        del storage.all()[data[0] + "." + data[1]]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, args):
        """ method that prints all the objects """
        all_objs = storage.all()
        if args:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] not in classes:
                print("** class doesn't exist **")
                return
            a = []
            for i, j in all_objs.items():
                if data[0] in i:
                    a.append(j)
            a = [str(i) for i in a]
            print(a)
        else:
            all_objs = [str(j) for j in all_objs.values()]
            print(all_objs)

    def do_update(self, args):
        """ method that updates an object """
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    if (data[0] + "." + data[1]) in all_objs:
                        if len(data) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(data) < 4:
                                print("** value missing **")
                            else:
                                if '"' in data[3]:
                                    setattr(storage.all()[data[0] +
                                            "." + data[1]], data[2],
                                            data[3].replace('"', ''))
                                    storage.all()[data[0] +
                                                  "." + data[1]].save()
                    else:
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
