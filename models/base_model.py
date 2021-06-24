#!/usr/bin/python3
"""Entry point for BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class for BaseModel.
    Instances of BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Instantiation for BaseModel.
        Args:
            *args: arguments.
            **kwargs: keyworded arguments.
        """
		time_attrs = ('created_at', 'updated_at')
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in time_attrs:
                    time_val = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, time_val)
                else:
                    setattr(self, k, v)
        else:
            current_time = datetime.now()
            self.id = str(uuid.uuid4())
            for a in time_attrs:
                setattr(self, a, current_time)
            models.storage.new(self)

