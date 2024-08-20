#!/usr/bin/python3
import json
import os


class FileStorage():
    _file_path = 'file.json'
    _objects = {}

    def all(self):
        ''' Returns the dictionary objects '''
        return self._objects

    def new(self, obj):
        '''
        Adds a new object to __objects
        But does it in a way in a special way
        key = <obj class name>.id
        value = obj

        '''
        if obj is not None:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self._objects[key] = obj

    def save(self):
        ''' Serialize objects to the JSON file '''
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                try:
                    json_objects = json.load(file)
                except json.JSONDecodeError:
                    json_objects = {}
        else:
            json_objects = {}

        for key, obj in self._objects.items():
            json_objects[key] = obj.to_dict()

        with open(self._file_path, 'w') as file:
            json.dump(json_objects, file, indent=4)


    def reload(self):
        ''' Deserialize the JSON file to __objects only if the JSON file
            exist
        '''
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                try:
                    json_objects = json.load(file)
                except json.JSONDecodeError:
                    print('Error: Json file not accepted')
                    return

                for key, value in json_objects.items():
                    cls_name = key.split('.')[0]
                    cls = globals().get(cls_name)
                    if cls:
                        self._objects[key] = cls(**value)
        else:
            print('File not found')
