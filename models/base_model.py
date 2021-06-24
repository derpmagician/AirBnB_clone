#!/usr/bin/python3
"""Entry point for BaseModel"""
import uuid
import models


class BaseModel:
    """Class for BaseModel.
    Instances of `BaseModel` autoupdate `updated_at` after
    any change through an overriden `__setattr__` method.
    """
    __str_fmt = "[{}] ({}) {}"

    def __init__(self, *args, **kwargs):
        """Instantiation for BaseModel.
        Args:
            *args: arguments.
            **kwargs: keyworded arguments.
        """
		pass

