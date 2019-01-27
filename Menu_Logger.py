import os
import sys
import datetime
import Add_Work_Logger
import Previous_Work_Logger
from time import gmtime, strftime, sleep
from collections import OrderedDict

def menu():
    clear()
    menu_loop()

def start():
    clear()
    user(name())
    show_time()
    clear()
    menu_loop()

def name():
    name = input("Enter full name please:  ")
    clear()
    return name

def user(name):
    current_time = datetime.datetime.now()
    if current_time < 12:
        print("Good morning {}, and welcome to the work logger.\n".format(name))
    elif 12 <= current_time < 18:
        print("Good afternoon {}, and welcome to the work logger.\n".format(name))
    else:
        print("Good evening {}, and welcome to the work logger.\n".format(name))

def show_time():
    the_time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    print("Current Time:", the_time)
    sleep(3)

def menu_loop():
    """Show the menu"""
    choice = None
    while choice != 'q':
        clear()
        print("Enter q to quit")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

menu = OrderedDict([
    ('a', Add_Work_Logger.add_work_log()),
    ('b', Previous_Work_Logger.previous_entries()),
    ('q', sys.exit()),
])

def clear():
    ''' Clear the page '''
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    start()