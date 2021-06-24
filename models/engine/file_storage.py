#!/usr/bin/python3
""" Module file_storage for the AirBnB console """
import json


class FileStorage:
    """ class that store information of the BaseModel Class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method that returns all objects """
        return self.__objects

    def new(self, obj):
        """ method that adds a new object """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ method that saves a new object """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            d = {i: j.to_dict() for i,
                 j in self.__objects.items()}
            json.dump(d, fp)

    def reload(self):
        """ method that loads the objectos from de file """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
                for i, j in data.items():
                    if "BaseModel" in i:
                        self.__objects[i] = BaseModel(**j)
                    elif "User" in i:
                        self.__objects[i] = User(**j)
                    elif "State" in i:
                        self.__objects[i] = State(**j)
                    elif "City" in i:
                        self.__objects[i] = City(**j)
                    elif "Amenity" in i:
                        self.__objects[i] = Amenity(**j)
                    elif "Place" in i:
                        self.__objects[i] = Place(**j)
                    elif "Review" in i:
                        self.__objects[i] = Review(**j)
        except Exception:
            pass
