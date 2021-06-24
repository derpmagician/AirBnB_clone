#!/usr/bin/python3
"""city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    class for City with attributes:
    state_id: The state id
    name: input name
    """
    state_id = ""
    name = ""
