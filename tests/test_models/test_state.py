#!/usr/bin/python3
"""test for state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """test the State class"""
    def setUp(self):
        """Sets up test methods."""
        FileStorage._FileStorage__file_path = "test_json"
        self.state = State()
        self.state.name = "Cundinamarca"
        self.state.save()

    def test_docstring_State(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """chekcing if State have attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)
        self.assertIsInstance(self.state, State)

    def test_attribute_types_State(self):
        """test attribute type for State"""
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(hasattr(self.state, "name"), True)

    def test_save_State(self):
        """test if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
