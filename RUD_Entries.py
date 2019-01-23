import csv
import datetime
import Menu_Logger
import Add_Work_Logger
import Confirm_Logger
from time import sleep


def delete_entry(task, time_spent, date, comments):
    while True:
        delete = input("Are you sure you want to delete this a) Yes or b) Now?  ")
        if not delete:
            input("Please choose whether you want to delete this or not... Press enter to continue...")
            continue
        elif delete.lower() in 'ab':
            if delete.lower() == 'a':
                task, time_spent, date, comments = (None,)*4
                Menu_Logger.menu()
                break
            elif delete.lower() == 'b':
                Menu_Logger.clear()
                Confirm_Logger.show_entries(task, time_spent, date, comments)
                break
            else:
                input("Invalid input... Please use either a) Yes of b) No... Press enter to continue...")


def save_entry(task, time_spent, date, comments):
    Menu_Work_log.clear() 
    with open('work_log.csv', 'a', newline='') as work_logger:
        fieldnames = ['Work Task', 'Time spent', 'Date', 'Comments']
        writer = csv.DictWriter(work_logger, fieldnames=fieldnames)
        filewriter.writerow({'Work Task': task, 'Time spent': time_spent, 'Date': date, 'Comments': comments})
            
    input(" Entry saved! Press enter to continue...")
    Menu_Logger.clear()
    Menu_Logger.menu()


def edit_entry(task, time_spent, date, comments):
    Menu_Work_log.clear()
    print("---------------------------- Edit Entry ----------------------------")
    change_entry = [task, time_spent, date, comments]
    entry_keys = iter(['Work Task', 'Time Spent', 'Date', 'Comments'])
    entry_items = iter([task, time_spent, date, comments])
    index = 0
    for _ in range(len(change_entry)):
        while True: 
            pf = next(entry_keys)
            print("Current {} : {}\n".format(pf, next(entry_items)))
            answer = input("Do you want to edit {}. a) Yes or b) No:  ". format(pf))
            if answer.lower() == 'a': 
                for i in change_entry: 
                    i = input("Change into:  ")
                    if index == 0: 
                        task = i
                    elif index == 1:
                        time_spent = i
                    elif index == 2: 
                        date = i
                    elif index == 3:
                        comments = i
                    break
                break
            elif answer.lower() == "b":
                break
            else: 
                input("Must answer with a) Yes or b) No. Press enter to continue... ")
                continue
        index += 1

Confirm_work_log.show_all_entries(task, time_spent, date, comments)