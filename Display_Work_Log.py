import Search_Date_Time
import Previous_Work_Logger
import Menu_Logger
import RUD_Entries
from time import sleep


def all_entries(searched_entries, entry_names):
    for n, e in zip(entry_names, searched_entries):
        print("{}: {}".format(n, e))

def results(searched_entries):
    count = 0
    while True:
        Menu_Logger.clear()
        names = iter(['Work Task', 'Time Spent', 'Date', 'Comments'])
        choices = ['a) Next', 'b) Previous', 'c) Edit', 'd) Delete', 'e) Return']
        print("---------------------------- Search Results ----------------------------")
        searched_item = searched_entries[count]
        entries = []
        for i in range(4):
            entry = next(names)
            print("{}: {}".format(entry, searched_item[entry]))
            entries.append(searched_item[entry])
        
        print("Result {} of {}".format(count+1, len(searched_entries)))
        if count == 0:
            choices.remove('b) Previous')
        try:
            if count == len(searched_entries) - 1:
                entry.remove('a) Next')
        except AttributeError:
            count -= 1

        options = ', '.join(choices) + ':  '
        choices_entry = input("{} to search menu\n".format(options)).strip()
        if choices_entry.lower() in 'abe' and choices_entry.lower() in choices:
            if choices_entry.lower() == 'b':
                count -= 1
                continue
            elif choices_entry.lower() == 'a':
                count += 1
                continue
            elif choices_entry.lower() == 'e':
                break
            elif choices_entry.lower() == 'c':
                RUD_Entries.edit_entry(entries[0], entries[1], entries[2], entries[3])
                break
            elif choices_entry.lower() == 'd':
                RUD_Entries.delete_entry(entries[0], entries[1], entries[2], entries[3])
                break
            else:
                input("Invalid input. Use the availabe options to navigate through this menu... Press enter to continue...")
                continue
        if choices_entry.lower() not in 'abe' and choices_entry.lower() not in options:
            input("Invalid input. Use the availabe options to navigate through this menu... Press enter to continue...")

    Menu_Logger.clear()
    Previous_Work_Logger.previous_entries()

    