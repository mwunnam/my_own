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
        '''checking for row win'''
        for i in range(0, 9, 3):
            if self.cells[i] == self.cells[i + 1] == self.cells[i + 2] != ' ':
                return self.cells[i]

        '''checkig for rows win'''
        for i in range(3):
            if self.cells[i] == self.cells[i + 3] == self.cells[i + 6] != ' ':
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









def print_header():
    print('Welcome to Tic_Tac_ Toe\n')

def ai_move(board, user)
    possible_moves = [i for i, cell in enumerate(board.cells) if cells == ' ']
    move = random.choice(possible_moves)
    board.b_update(move, user)

def refresh_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    board.b_display()

def play_again(option):
        if option == 'Y':
            board.b_clear()
            refresh_board()
        elif option == 'N':
            return

def game_loop(player_1, player_2):
    current_player = player_1
    refresh_board()

    while True:
        '''Get Player_1's input'''

        if current_player == player_1:
            x_choice = int(input(f"{player_1} pick your choice (0-8):>> "))
            while not board.b_update(x_choice, 'X'):
                print('cell taken choice under number')
                x_choice = int(input("pick a choice (0-8):>> "))

            refresh_board()

        else:
            if player_2:
                o_choice = int(input(f"{player_2} pick a choice (0-8):>> "))
                while not board.b_update(o_choice, 'O'):
                    print('cell taken choice under number')
                    o_choice = int(input("pick a choice from (0-8):>> "))
            else:
                if player_2 is None:
                    player_2 = 'AI'
                    print('{play_2} pick your choice (0-8):>> ')
                    ai_move(board, '0')


            refresh_board()

            winner = board.win_checker()
            if winner:
                print(f'{winner} wins!')
                option = input('Press Y to play again or N to quit>> ')
                play_again(option)

            if board.tie_checker():
                print("It's a tie")
                option = input('Press Y to play again or N to quit>>  ')
                play_again(option)


        if current_player == player_1:
            current_player = player_2
        else:
            current_player == player_2

        '''
        except ValueError:
            print('Enter a valid number (0-8).')
        except IndexError:
            print('Enter a number within the range (0-8).')
        '''



board = BaseModel()
print_header()
print('Choose Game Mode:')
print('1. Player vs Player:')
print('2. Player vs AI:')
mode = input('Enter 1 or 2: ')

if mode == '1':
    player_1 = input("Enter Player_1's Name>> ")
    player_2 = input("Enter Player_2's Name>> ")
    game_loop(player_1, player_2)
elif mode == '2':
    player_1 = input("Enter Player_1's Name>> ")
    player_2 = 'AI'
    game_loop(player_1, player_2)
else:
    print('Choose a valid number to play the came')
