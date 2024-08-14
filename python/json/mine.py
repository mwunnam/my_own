#!/usr/bin/python3

import json

person = '{"name": "Michael", "surname": "Wunnam", "age": 32}'

with open("person.json", "w") as json_file:
    person = json_file.write(person)

with open("person.json", "r") as json_file:
    person = json_file.read()
    person = json.loads(person)
    person['name'] = "Wunnam"
    person['surname'] = "Michael"
    person['age'] = 31


    name = person['name']
    surname = person['surname']
    age = person['age']
    print(f'I am {name} {surname} and I am {age} years old')
    person

