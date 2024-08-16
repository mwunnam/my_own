#!/usr/bin/python3
""" Console to myAirBnB """
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        '''
        Create an instace of BaseModel and save it to the json file
        Checking for class name missing and not exiting
        '''
        if not line:
            print('** class name missing ** ')
            return

        class_name = line.strip()
        cls = globals().get(class_name, None)
        if cls is None:
            print("** calss doesn'n exist **")
            return

        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        '''
        '''
        if not line:
            print('** class name missing **')
            return

        else:
            parts = line.split()
            if len(parts) < 2:
                print('** instance id missing **')
                return

            class_name, instance_id = parts[0], parts[1]
            if class_name is None:
                print('** Class name missing **')
                return

            if instance_id is None:
                print('** instance id missing **')
                return

            cls = globals().get(class_name)
            if cls is None or not issubclass(cls, BaseModel):
                print("** calss doesn't exist **")
                return

            key = f'{class_name}.{instance_id}'
            instance = storage._objects.get(key)
            if instance is None:
                print('** no instance found **')
                return

            print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
