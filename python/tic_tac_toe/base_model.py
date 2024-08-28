#!/usr/bin/python3
""" Base Model for Tic Tact Toe """


class BaseModel:
    """Base Model with all the needed functions """
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


    def b_display(self):
        print(f'\t|{self.cells[0]}|{self.cells[1]}|{self.cells[2]}|')
        print('\t-------')
        print(f'\t|{self.cells[3]}|{self.cells[4]}|{self.cells[5]}|')
        print('\t-------')
        print(f'\t|{self.cells[6]}|{self.cells[7]}|{self.cells[8]}|')


    def b_clear(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def b_update(self, choice, user=""):
        if self.cells[choice] is None:
            self.cells[choice] = user

board = BaseModel()

def print_header():
    print('Welcome to Tic_Tac_ Toe\n')

def refresh_board():
    print_header()
    board.b_display()


refresh_board()
while True:

    '''Get X input'''
    x_choice = 4
    board.b_update(x_choice, 'X')



