#!/usr/bin/python3
""" Console to myAirBnB """
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    Command interpreter for myAirbnb project
    '''
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''
        Ctrl + D close the console gracefully
        Handle end of file and close program
        '''
        print('Closing the program')
        return True

    def do_quit(self, line):
        '''
        To quit the program
        quit <enter>
        '''
        return True

    def emptyline(self):
        '''
        Overides the default behavior for an empty line.
        '''
        pass

    def do_help(self, line):
        '''
        Help for the program
        help <enter>
        or help <command>
        '''
        if not line:
            print(cmd.Cmd.do_help(self, line))
        else:
            command = getattr(self, f'do_{line}', None)

            if command:
                print(command.__doc__)

            else:
                print(f'*** No help is avaliable for {line}')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
