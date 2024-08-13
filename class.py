#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    facility = "COLANGE"

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = (datetime.datetime.now())
        self.updated_at = (datetime.datetime.now())

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_ = (datetime.datetime.now())


    def to_dic(self):
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        dict_copy['__class__ '] = self.__class__.__name__
        return dict_copy
