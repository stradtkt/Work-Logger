import csv
import Menu_Logger
import Search_Date_Time

def previous_entries():
    date = Search_Date_Time.Date()

while True:
    Menu_Logger.clear()
    print("---------------------------- Lookup Previous Entries ----------------------------")
    print(""" 
        a) Search By Date
        b) Search By Time Spent
        c) Search By Regex Or Text
        d) Go Back
    """)
    choice = input("How would you like to search:  ").strip()
    if choice.lower() in "abcd":
        if choice.lower() == 'a':
            date.date_options()
            break
        elif choice.lower() == 'b':
            Search_Date_Time.search_time()
            break
        elif choice.lower() == 'c':
            Search_Date_Time.search_text()
            break
        elif choice.lower() == 'd':
            Menu_Logger.clear()
            Menu_Logger.menu()
            break
    else:
        input("Invalid input... Choose from the menu and please try again... Please press enter...")
        continue

def get_entries():
    with open('work_logger.csv', 'r') as work_logger:
        fieldnames = ['Work Task', 'Time Spent', 'Date', 'Comments']
        reader = csv.DictReader(work_logger, fieldnames=fieldnames)
        entries = list(reader)
        return entries
