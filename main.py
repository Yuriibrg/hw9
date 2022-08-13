from parser import parse_command
from collections import defaultdict

BOOK = {}

def main():
    user_com = ''
    while user_com != ".":
        user_com = input("Enter str:")
        user_command = parse_command(user_com)
        contact_book(user_command)




def user_command_hello(user_command):

    return print("How can I help you?")



def user_command_add(user_command):

    name = user_command[1]
    number = user_command[2]
    BOOK[name] = number
    return print(BOOK)




def user_command_change(user_command):

    pass


def user_command_phone(user_command):
    pass


def user_command_show_all(user_command):
    pass


def user_command_good_bye(user_command):
    return print('Fuck')

user_commands = {

    "hello": user_command_hello,
    "add": user_command_add,
    "change": user_command_change,
    "phone": user_command_phone,
    "show all": user_command_show_all,
    "good bye": user_command_good_bye,
}

def contact_book(user_command):

    for command, handle in user_commands.items():
        if command == user_command[0]:
           handle(user_command)

    return handle


if __name__ == '__main__':

    main()