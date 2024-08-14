#!/usr/bin/python3


age = int(input('Enter you age: '))

if age < 0:
    print('Please enter a valid age.')
elif age < 18:
    print('You are a minor')
elif age >= 18 and age < 65:
    print('you are an adult')
else:
    print('You are a senior citizen.')
