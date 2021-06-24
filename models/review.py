#!/usr/bin/python3
"""review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review with attributes:
    place_id: place id
    user_id: user id
    text: review description
    """
    place_id = ""
    user_id = ""
    text = ""
