#!/usr/bin/env python3
'''
important things to keep in the __init__ file
'''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

''' Create a unique FileStorage instace '''
storage = FileStorage()

'''
Optionally, specify the file path if needed
storage.__file_path = 'file.json'
'''

''' Call the reload method to load any existing data from the file '''
storage.reload()

'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
'''
