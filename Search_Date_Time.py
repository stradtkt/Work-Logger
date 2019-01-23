import Previous_Work_Logger
import Add_Work_Logger
import Display_Work_Log
import Menu_Logger
import datetime
import re
from time import sleep


class Date:
    def date_options(self):
        while True:
            Menu_Logger.clear()
            entries = Previous_Work_Logger.get_entries()
            choices = input("You have two options... You can choose between search through a) exact date or b) range of date:  ")
            if choices.lower() == 'a':
                Date.search_exact_date(entries)
                break
            elif choices.lower() == 'b':
                Date.search_by_date_range()
                break
            else:
                input("Invalid input... Press enter to continue...")
                continue
    
    def search_exact_date(entries):
        Menu_Logger.clear()
        dates = Date.get_dates(entries)
        Date.print_entry_dates(dates)
        searched = []
        while True:
            search_date = input("Enter a date (dd-mm-yyyy):  ").strip()
            if not search_date:
                input("Enter a date.... Press enter to continue....")
                continue
            if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}$', search_date):
                input("Invalid date... Your date must be in the right format... Press enter to continue....")
                continue
            if search_date not in entries_dates:
                input("Enter valid date... Pick a date from the above.... Press enter to continue... ")
                continue
            else:
                for e in entries:
                    if e['Date'] == search_date:
                        searched.append(e)
                Display_Work_Log.results(searched)
                break
    
    def get_dates(entries):
        search_date = []
        for e in entries:
            if e['Date'] not in search_date:
                search_date.append(e['Date'])
        dates = sorted(search_date)
        return dates

    def print_entry_dates(dates):
        print("---------------------------- Dates ----------------------------")
        for d in dates:
            print('\n', d)

    def search_by_date_range():
        Menu_Logger.clear()
        entries = Previous_Work_Logger.get_entries()
        entry_dates = Date.get_dates(entries)
        searched_entries = []
        searched_dates = []

        while True:
            Menu_Logger.clear()
            Date.print_entry_dates(entry_dates)
            print("---------------------------- a) To return ----------------------------")
            ranged = input('Choose a date like this (dd-mm-yyyy to dd-mm-yyyy):  ')
            if not ranged:
                input("Enter a date range... Press enter to continue...")
                continue

            if ranged.lower() == 'a':
                Previous_Work_Logger.previous_entries()
                break

            if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}\s?to\s?[0-9]{2}-[0-9]{2}-[0-9]{4}$', ranged):
                input("Invalid date range... Press enter to continue... ")
                continue
            else:
                ranged = [date.strip() for d in ranged.split("to")]
                if ranged[0] not in entry_dates or ranged[-1] not in entry_dates:
                    input("Sorry that input has failed as a correct range... Please enter the date again... Press enter to continue...")
                    continue

                for entry in entry_dates:
                    if entry >= ranged[0] and entry <= ranged[-1]:
                        searched_dates.append(entry)
                
                for e in entries:
                    if e['Date'] in searched_dates:
                        searched_entries.append(entry)
                
                Display_Work_Log.results(searched_entries)
                break
    

    def search_time():
        Menu_Logger.clear()
        entries = Previous_Work_Logger.get_entries()
        new_time = []
        searched = []
        for e in entries:
            time_spent = e['Time Spent']
            time_spent = int(time_spent)
            time_spent = datetime.timedelta(minutes=time_spent)
            time_spent = str(time_spent)
            time_spent = time_spent[:-3]
            if time_spent not in new_time:
                new_time.append(time_spent)
        
        while True:
            Menu_Logger.clear()
            print("---------------------------- Current Times ----------------------------")
            for new in new_time:
                print("---------------------------- "+new+" ----------------------------")
                sleep(1)
            
            search_time = Add_Work_Logger.time_spent()
            search_time = str(search_time)
            for e in entries:
                if e['Time Spent'] == search_time:
                    searched.append(e)
            if not searched:
                input("Sorry, no task available... Please press enter to continue...")
                continue
            else:
                Display_Work_Log.results(searched)
                break
    
    def search_text():
        pass