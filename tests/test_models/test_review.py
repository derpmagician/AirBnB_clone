#!/usr/bin/python3
"""test for review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """test the place class"""

    def setUp(self):
        """Sets up test methods."""
        FileStorage._FileStorage__file_path = "test_json"
        self.rev = Review()
        self.rev.place_id = "1111"
        self.rev.user_id = "2222"
        self.rev.text = "3333"
        self.rev.save()

    def test_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)
        self.assertIsInstance(self.rev, Review)

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)
        self.assertNotEqual(hasattr(self.rev, "name"), True)

    def test_save_Review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
