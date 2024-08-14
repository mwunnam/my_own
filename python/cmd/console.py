#!/usr/bin/python3

import cmd


class MyConsole(cmd.Cmd):
    '''Simple console to understand how it works'''
    def do_greet(self, name):
        '''Greeting the user'''
        if name:
            print(f'Hello {name}')
        else:
            print('Hello there')

    def help_greet(self):
        print('\n'.join(['greet [name_of_person]',
                        'Hello name_of_person'
                    ]))
        print('if no name given')
        print('\n'.join(['greet', 'Hello there']))

    def do_EOF(self, line):
        print("Closing")
        return True


if __name__ == '__main__':
    MyConsole().cmdloop()
