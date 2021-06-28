#!/usr/bin/python3
"""Entry point for BaseModel"""
import uuid
from datetime import datetime
from models import storage
dformat = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """Class for BaseModel"""

    def __init__(self, *args, **kwargs):
        """Instantiation for BaseModel.
        Args:
            *args: arguments.
            **kwargs: keyworded arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, dformat))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """human readable method"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates pblic instance attribute updated_at with the curr dttime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        creates dic of the class and returns a dic of all the k val in __dict__
        """
        mydict = self.__dict__.copy()
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        mydict["__class__"] = self.__class__.__name__

        return mydict
