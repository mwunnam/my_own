#!/usr/bin/python3
""" Console to myAirBnB """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


storage.reload()

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

    def do_destroy(self, line):
        if line:
            parts = line.split()
            if len(parts) < 2:
                print('** instance id missing **')
                return

            class_name, instance_id = parts[0], parts[1]
            cls = globals().get(class_name)
            if cls is None:
                print("** class name does'nt exist **")
                return

            key = f'{class_name}.{instance_id}'
            instance = storage._objects.get(key)

            if instance is None:
                print("** no instance found **")
                return

            storage._objects.pop(instance)
            storage._objects.save()
        else:
            print('** class name missing **')
            return

    def do_all(self, line):
        if line:
            parts = line.split()
            class_name = parts[0]

            cls = globals().get(class_name)

            if cls is None:
                print("** class doesn't exist **")
                return

            result = [str(obj) for key, obj in storage._objects.items() if
            key.startswith(f'{class_name}.')]
        else:
            result = [str(obj) for obj in storage.all().values()]

        print(result)



    def do_update(self, line):
        if line:
            parts = line.split(" ", 3)
            if len(parts) < 2:
                print('** instance id missing **')
                return
            if len(parts) < 3:
                print('** attribute name is missing **')
                return
            if len(parts) < 4:
                print('** attribute value is missing **')
                return

            class_name, id, attribute_name, attribute_value = parts

            cls = globals().get(class_name)
            if cls is None:
                print("** class doesn't exist **")
                return

            key = f'{class_name}.{id}'
            instance = storage._objects.get(key)
            if instance is None:
                print('** no instance found **')
                return

            if attribute_name in ['id', 'created_at', 'updated_at']:
                print('** cannot update these attributes **')
                return

            value_type = type(getattr(instance, attribute_name, str))
            if value_type == int:
                attribute_value = int(attribute_value)
            elif value_type == float:
                attribute_value = float(attribute_value)
            elif value_type == str:
                attribute_value = attribute_value.strip('"')


            setattr(instance, attribute_name, attribute_value)

            storage._objects[key] = instance
            storage.save()

        else:
            print("** class name is missing **")
            return

    def all_command(self, class_name):
        '''Handle the <class_name>.all() command.'''
        cls = globals().get(class_name)
        if cls:
            results = [str(obj) for key, obj in storage._objects.items() if
                        key.startswith(f'{class_name}.')]
            print(results)
        else:
            print("** class doesn't exist **")
            return

    def count_command(self, class_name):
        cls = globals().get(class_name)
        if cls:
            count = sum(1 for obj in storage._objects.values() if
                    isinstance(obj, cls))
            print(count)
        else:
            print('** class instance not found **')
            return


    def show_command(self, class_name, instance_id):
        cls = globals().get(class_name)
        if cls:
            key = f'{class_name}.{instance_id}'
            instance = storage._objects.get(key)

            if instance is None:
                print('** no instance found **')
                return
            else:
                print(instance)
        else:
            print("** class doesn't exist ***")
            return


    def default(self, line):
        '''Handling custom / unrecorgnized commands.'''
        if '.' in line:
            parts = line.split('.')
            class_name = parts[0]
            cmd = parts[1]

            if cmd == 'all()':
                self.all_command(class_name)

            elif cmd == 'count()':
                self.count_command(class_name)

            elif cmd.startswith('show(') and cmd.endswith(')'):
                instance_id = cmd[len('show('): - 1].strip('"')
                self.show_command(class_name, instance_id)

            else:
                print(f'*** Unknown syntax: {line}')
        else:
            print(f'*** Unknown syntax: {line}')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
