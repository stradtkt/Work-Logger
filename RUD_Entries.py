import csv
import datetime
import Menu_Logger
import Add_Work_Logger
import Confirm_Logger
from time import sleep


def delete_entry(task, time_spent, date, comments):

    while True:
        delete = input("Are you sure you want to delete, y) Yes or n) No? ")
        if not delete:
            input("Please confirm whether to delete or not. Press enter to continue... ")
            continue

        elif delete.lower() in "yn":
            if delete.lower() == 'y':
                task, time_spent, date, comments = (None,)*4
                Menu_Logger.menu()
                break

            elif delete.lower() == 'n':
                Menu_Logger.clear()
                Confirm_Logger.show_entries(task, time_spent, date, comments)
                break
        else:
            input("Invalid input. Please use either 'y' or 'n'. Press enter to continue... ")


def save_entry(task, time_spent, date, comments): 
    """Saves the user's entries """
    Menu_Logger.clear() 

    with open('work_log.csv', 'a', newline='') as csvfile: # Make a CSV file folder 
        fieldnames = ['Task name', 'Time spent', 'Date', 'Comments']
        filewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        filewriter.writerow({
            'Work Task': task,
            'Time spent': time_spent,
            'Date': date,
            'Comments': comments})
            
    input(" Entry saved! Press enter to continue...")
    Menu_Logger.clear()
    Menu_Logger.menu()
       

def edit_entry(task, time_spent, date, comments):
    """Allows the user to edit their entry"""
    Menu_Logger.clear()
    print("------------------------------------------------------------- Edit Entry -------------------------------------------------------------")
    change_entry = [task, time_spent, date, comments]