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
        pass

    def print_entry_dates(dates):
        pass

    def search_by_date_range():
        pass