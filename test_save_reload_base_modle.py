#!/usr/bin/python3

from models import storage
from models.base import BaseModel


all_objs = storage.all()
print('__Reloaded Objects __')
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print('--Create a new Object --')
my_model = BaseModel()
my_model.name = 'My_First_Model'
my_model.my_number = 89
my_model.save()
print(my_model)
