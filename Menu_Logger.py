import datetime
import sys
import os

from time import gmtime, sleep, strftime

from Add_Work_Logger import add_log
from Previous_Work_Logger import show_previous_entries


def clear():
    """Clear The Screen"""
    try:
        os.system('cls')
    except:
        os.system('clear')

def start_app():
    clear()
    welcome_user(ask_for_name())
    show_time()
    clear()
    show_menu()

def menu():
    """Initiates the menu"""
    clear()
    show_menu()

def ask_for_name():
    name = input("Enter your name please: \n")
    clear()
    return name

def show_time():
    print("Current Time\n")
    time = strftime("%a, %d %b %Y %H:%M:%S ", gmtime())
    print(time)
    sleep(3)

def welcome_user(name):
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        print("Good morning {}, and welcome to my work log. \n".format(name))
    elif 12 <= current_time.hour < 18:
        print("Good afternoon {}, and welcome to my work log. \n".format(name))
    else:
        print("Good evening {}, and welcome to my work llog. \n".format(name))
    sleep(4)

def show_menu():
    while True:
        print("Menu ")
        print(""" 
                [A]dd a new entry
                [L]ookup previous entries
                [Q]uit
                """)
        option = input("\n What choice would you like to make? \n").strip()
        if option.upper() in "ALQ":
            if option.upper() == 'A':
                Add_Work_Logger.add_log()
                break
            elif option.upper() == 'L':
                Previous_Work_Logger.show_previous_entries()
                break
            elif option.upper() == 'Q':
                clear()
                sys.exit
                break
        else:
            input("\n Invalid option. Please use the menu correctly. Use A Q or L. Press enter to continue...")
            show_menu()
            break


if __name__ == '__main__':
    start_app()