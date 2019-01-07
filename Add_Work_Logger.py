import datetime
import re

import Menu_Logger
import Confirm_Logger

def add_log():
    Menu_Logger.clear()
    print("        " + "            New Work Log       " + "           ")
    print("If you would like to go back press 'back' ")
    while True:
        task = input("Please enter the task name for the job:   ").strip()
        if not task:
            input("Your task cannot be empty, please press enter and try again...")
            continue
        elif task.lower() == "back":
            Menu_Logger.menu()
            break
        else:
            break

def task_comments():
    Menu_Logger.clear()
    comments = input("Fill in comments about your work task if you would like.")
    if comments == "":
        comments = None
        return comments
    else:
        return comments

def ask_time_spent():
    Menu_Logger.clear()
    while True:
        time_spent = input("Please enter the amount of time you spent on the job like this hh:mm: \n").strip()
        if not re.match(r'\d{1,2}:\d{2}$', time_spent):
            input("Invalid amount of time spent on the job.  The regex didn't match up please try again. Press enter to continue...")
            continue
        elif re.match(r'^\d{1,2}:\d{2}$', time_spent):
            time_split = time_spent.split(":")
            if (int(time_split[0]) < 1) and (int(time_split[1]) < 1):
                input("Time spent cannot be 0 hours and 0 minutes. Please press enter to continue...")
                continue
            elif int(time_split[0]) > 24:
                input("Time spent cannot be more than 24 hours.  Please press enter to continue...")
                continue
            elif (int(time_split[0]) == 24) and (int(time_split[1]) > 0):
                input("Time spent cannot be more than 24 hours please press enter to continue...")
                continue
            

