#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    facility = "COLANGE"

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            self.created_at = datetime.strptime(self.created_at,'%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.upadated_at,'%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)




    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()


    def to_dict(self):
        dict_copy = self.__dict__.copy()
        if isinstance(dict_copy.get('created_at'), datetime):
            dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        if isinstance(dict_copy.get('updated_at'), datetime):
            dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
