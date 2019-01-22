import os
import sys
import datetime
import Add_Work_Logger
import Previous_Work_Logger
from time import gmtime, strftime, sleep


def menu():
    pass

def start():
    clear()
    user(name())
    show_time()
    clear()
    display_menu()

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

def display_menu():
    ''' Menu for the Application '''
    while True:
        print(''' 
        
        Menu
        a) Add New Entry
        b) Lookup Previous Entries
        c) Quit
        
        ''')
        choice = input("\n\nWhat would you like to do?  ").strip()
        if choice.lower() in "abc":
            if choice.lower() == 'a':
                Add_Work_Logger.add_work_log()
                break
            elif choice.lower() == 'b':
                Previous_Work_Logger.previous_entries()
                break
            elif choice.lower() == 'c':
                input("Thank you come again... Press enter to leave...")
                clear()
                sys.exit()
                break
        else:
            input("That is an invalid option... Please choose from the 3 choices a, b or c... Press enter to continue...")
            display_menu()
            break


def clear():
    ''' Exit the system '''
    try:
        os.system('cls')
    except:
        os.system('clear')


if __name__ == '__main__':
    start()