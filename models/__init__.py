#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

store_type = os.getenv('HBNB_TYPE_STORAGE')

if store_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

# Enables us perform wildcard package importation
__all__ = ['Amenity', 'City', 'State', 'Place', 'Review', 'User', 'storage']
