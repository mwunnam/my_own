
import json

person_json = '{"name":"Michael", "surname":"Issahaku", "age":32}'
print(type(person_json))

person = json.loads(person_json)
person['name'] = 'Chrity'
person['surname'] = 'Chenty'
person['age'] = 30

new_person_json = json.dumps(person)
print(new_person_json)

with open('person.json', 'w') as json_file:
    json_file.write(new_person_json)
    print('Saved succesfully!')

with open("person.json", "r") as json_file:
    person = json_file.read()
    print(person)
    person_converted = json.loads(person)

    name = person_converted['name']
    surname = person_converted['surname']
    age = person_converted['age']

    print(f'I am {name} {surname} and I am {age} yearsof age')
print("____________________________________________________________")

with open("person.json", "w") as json_file:
    person_converted['name'] = 'Gedion'
    person_converted['surname'] = 'Sugri'
    person_converted['age'] = 36

    name = person_converted['name']
    surname = person_converted['surname']
    age = person_converted['age']



    new_person_json = json.dumps(person_converted, indent=2)
    json_file.write(new_person_json)
    print('Save!')
    print(f'I am {name} {surname} and I am {age} yearsof age')

