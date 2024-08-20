#!/usr/bin/python3
import os
import json

class BaseModel():
    pass

def reload():
    objects = {}
    if os.path.exists('file.json'):
        with open('file.json', 'r') as file:
            json_objects = json.load(file)

            for key, value in json_objects.items():
                cls_name = key.split('.')[0]
                cls = globals().get(cls_name)
                objects[key] = cls(**value)

        print(objects)
    else:
        pass


if __name__ == '__main__':
    reload()
