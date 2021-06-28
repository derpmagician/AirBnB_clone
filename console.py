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

    def default(self, args):
        """Method when the command is not recognized"""
        data = args.split('.')
        if len(data) >= 2:
            if data[1][:3] == "all":
                self.do_all(data[0])
            elif data[1][:5] == "count":
                self.do_count(data[0])
            elif data[1][:4] == "show":
                aux = data[1].split('(')
                if len(aux) >= 2:
                    self.do_show(data[0] + ' ' + aux[1][1:-2])
                else:
                    print("** no instance found **")
            elif data[1][:7] == "destroy":
                aux = data[1].split('(')
                if len(aux) >= 2:
                    self.do_destroy(data[0] + ' ' + aux[1][1:-2])
                else:
                    print("** no instance found **")
            elif data[1][:6] == "update":
                aux = data[1].split('(')
                key = aux[1].split(' ')
                if "{" in aux[1] and "}" in aux[1]:
                    a = re.search(r"(?<=\{)([^\}]+)(?=\})", aux[1]).group(0)
                    try:
                        a = eval("{" + a + "}")
                        b = list(a.keys())
                        c = list(a.values())
                        if len(b) == 1:
                            self.do_update(data[0] + ' ' + key[0][1:-2] + ' ' +
                                           b[0] + ' ' + '"' + str(c[0]) + '"')
                        elif len(b) == 2:
                            self.do_update(data[0] + ' ' + key[0][1:-2] + ' ' +
                                           b[0] + ' ' + '"' + str(c[0]) + '"')
                            self.do_update(data[0] + ' ' + key[0][1:-2] + ' ' +
                                           b[1] + ' ' + '"' + str(c[1]) + '"')
                    except Exception:
                        print(Exception.Exception)
                elif len(aux) >= 2 and len(key) == 3:
                    self.do_update(data[0] + ' ' + key[0][1:-2] + ' ' +
                                   key[1][1:-2] + ' ' + key[2][:-1])
                elif len(key) > 3:
                    self.do_update(data[0] + ' ' + key[0][1:-2] + ' ' +
                                   key[1][2:-2] + ' ' + key[2][:-1] + ' ' +
                                   key[3][1:-2] + ' ' + '"' +
                                   key[4][1:-2] + '"')
                else:
                    print("** no instance found **")
        else:
            cmd.Cmd.default(self, args)

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
