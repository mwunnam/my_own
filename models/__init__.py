#!/usr/bin/env python3
'''
important things to keep in the __init__ file
'''
from models.engine.file_storage import FileStorage

''' Create a unique FileStorage instace '''
storage = FileStorage()

'''
Optionally, specify the file path if needed
storage.__file_path = 'file.json'
'''
''' Call the reload method to load any existing data from the file '''
storage.reload()
