#!/usr/bin/python3
""" This module handles initialization """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
