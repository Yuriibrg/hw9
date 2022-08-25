from contact_book import BOOK
from parser import parse_command
from decor import input_error


def main():
    user_com = ''
    while user_com != ".":
        user_com = input("Enter str:")
        user_command = parse_command(user_com)
        contact_book(user_command)


def user_command_hello(user_command):

    return print("How can I help you?")


@input_error
def user_command_add(user_command):
    # try:
    name = user_command[1]
    number = user_command[2]
    if not name in BOOK.keys():
        BOOK[name] = number
    else:
        print("Такий контакт вже є у Вашій книзі")

    return BOOK
    # except IndexError:
    #     print('Bad command format. Required arguments: add [name] [number]')


@input_error
def user_command_change(user_command):

    name = user_command[1]
    number = user_command[2]

    if name in BOOK.keys():
        BOOK[name] = number
    else:
        return print("Такого контакта нема у Вашій книзі")


def user_command_phone(user_command):

    name = user_command[1]
    for contact, tel in BOOK.items():
        if name == contact:
            print(tel)
        else:
            print("Такий контакт не зареєстровано у Вашій книзі")


def user_command_show_all(user_command):

    user_command[0] = " ".join(user_command)

    return print(BOOK)


def user_command_good_bye(user_command):
    print('Good bye!')
    exit()


user_commands = {

    "hello": user_command_hello,
    "add": user_command_add,
    "change": user_command_change,
    "phone": user_command_phone,
    "show": user_command_show_all,
    "good": user_command_good_bye,
    "exit": user_command_good_bye,
    "close": user_command_good_bye,
}


def contact_book(user_command):

    for command, handle in user_commands.items():
        if command == user_command[0]:
            handle(user_command)

    return handle


if __name__ == '__main__':

    main()