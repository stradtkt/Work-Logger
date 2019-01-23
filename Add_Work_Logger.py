import datetime
import re

import Menu_Logger
import Confirm_Logger

def add_log():
    Menu_Logger.clear()
    print("------------------------------- New work log -------------------------------")
    print("If you like to go back press 'back' ")
    while True:
        task_name = input("Enter your task name please: ").strip()
        if not task_name:
            input(" My apologies, but your task name can't be empty. Press enter to continue... ")
            continue
        elif task_name.lower() == "back":
            Menu_Logger.menu()
            break
        else:
            break

    Confirm_work_log.show_entries(task_name, ask_time_spent(), ask_enter_date(), ask_task_comments())


def ask_task_comments():
    Menu_Logger.clear()
    comments = input("Fill in comments about your task if you like( It's optional):  ")
    if comments == "": 
        comments = None
        return comments
    else: 
        return comments


def ask_time_spent():
    Menu_Logger.clear()
    while True:
        time_spent = input("Time spent? Please enter like this: hh:mm :> ").strip()
        if not re.match(r'^\d{1,2}:\d{2}$', time_spent):
            input(" Invalid duration. Your duration must be in the format hh:mm. Press enter to continue... ")
            continue
        elif re.match(r'^\d{1,2}:\d{2}$', time_spent):
            time_spent_split = time_spent.split(':')
            # check to see if duration is not 0
            if (int(time_spent_split[0]) < 1) and (int(time_spent_split[1]) < 1):
                input(" Time spent cannot be of 0 hour and 0 minute. Press enter to continue... ")
                continue
                # check to see if hour part of time is not more than 24
            elif int(time_spent_split[0]) > 24:
                input(" Time spent cannot be more than 24 hours. Press enter to continue... ")
                continue
                # check to see if duration is not more than 24
            elif (int(time_spent_split[0]) == 24) and (int(time_spent_split[1]) > 0):
                input(" Time spent cannot be more than 24 hours. Press enter to continue... ")
                continue
                # check to see if duration is not more than 24
            elif (int(time_spent_split[0]) == 23) and (int(time_spent_split[1]) > 60):
                input(" Time spent cannot be more than 24 hours. Press enter to continue... ")
                continue
            else:
                time_spent = (int(time_spent_split[0]) * 60) + (int(time_spent_split[1]))
                return time_spent
    

 

def ask_enter_date():
        """Asks for date and validates it"""
        Menu_Logger.clear()
        while True:
            task_date = input("When was this task performed? Date format: dd-mm-yyyy: ").strip()
            if task_date.lower() == "back":
                Menu_Logger.menu()
                break

            try:
                task_date = datetime.datetime.strptime(task_date, "%d-%m-%Y")
                if task_date.date() > datetime.datetime.today().date():
                    input(" Sorry, date can't be later than today's date. Press enter and provide a correct date ")
                    continue
            except ValueError:
                input(" Sorry, not a valid date... Press enter and provide a correct date... ")
                continue
            except Exception: 
                input("Something went wrong. Please try again... Press enter to continue...")
            else:
                return task_date.strftime("%d-%m-%Y")
            

