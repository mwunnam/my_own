import cmd

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
       return f'User: {self.username}, Email: {self.email}'

class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def list_users(self):
       return self.users


'''CMD Part'''
class UserCmd(cmd.Cmd):
    prompt = 'UserCmd> '
    intro = 'Welcome to the User Manager CLI. Type "help" to list available commands.'

    def __init__(self):
        super().__init__()
        self.manager = UserManager()

    def do_create_user(self, arg):
        args = arg.split()
        if len(args) != 2:
            print('Usage: create_user <username> <email>')
            return
        username, email = args
        user = self.manager.create_user(username, email)
        print(f'User cerated: {user}')

    def do_list_users(self, arg):
        users = self.manager.list_users()
        if users:
            print("Users:")
            for user in users:
                print(user)
        else:
            print('No users found.')

    def do_quit(self, arg):
        '''Exit the program.'''
        print("Exiting...")
        return True

if __name__ == "__main__":
    UserCmd().cmdloop()
