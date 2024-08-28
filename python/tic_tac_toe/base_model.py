#!/usr/bin/python3
""" Base Model for Tic Tact Toe """

import os


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
        if self.cells[choice] == ' ':
            self.cells[choice] = user
            return True
        else:
            return False

    def win_checker(self):
        '''checking for column win'''
        for i in range(0, 9, 3):
            if self.cells[i] == self.cells[i + 3] == self.cells[i + 6] != ' ':
                return self.cells[i]

        '''checkig for rows win'''
        for i in range(3):
            if self.cells[i] == self.cells[i + 1] == self.cells[i + 2] != ' ':
                return self.cells[i]

        if self.cells[0] == self.cells[4] == self.cells[8] != ' ':
            return self.cells[0]
        if self.cells[2] == self.cells[4] == self.cells[6] != ' ':
            return self.cells[2]
        return None


    def tie_checker(self):
        if ' ' not in self.cells:
            return True
        return False






board = BaseModel()


def print_header():
    print('Welcome to Tic_Tac_ Toe\n')


def refresh_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    board.b_display()


refresh_board()
while True:
    '''Get X input'''
    try:
        x_choice = int(input("User 'X' pick a choice (0-8): "))
        while not board.b_update(x_choice, 'X'):
            print('cell taken choice under number')
            x_choice = int(input("pick a choice (0-8): "))

        refresh_board()

        winner = board.win_checker()
        if winner:
            print(f'{winner} wins!')
            break

        if board.tie_checker():
            print("It's a tie")
            break

    except ValueError:
        print('Enter a valid number (0-8).')
    except IndexError:
        print('Enter a number within the range (0-8).')

    '''Get O input'''
    try:
        o_choice = int(input("User 'O' pick a choice (0-8): "))
        while not board.b_update(o_choice, 'O'):
            print('cell taken choice under number')
            o_choice = int(input("pick a choice from (0-8): "))

        refresh_board()

        winner = board.win_checker()
        if winner:
            print(f'{winner} wins!')
            break

        if board.tie_checker():
            print("It's a tie")
            break

    except ValueError:
        print('Enter a valid number (0-8).')
    except IndexError:
        print('Enter a number within the range (0-8).')
