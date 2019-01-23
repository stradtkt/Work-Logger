import Add_Work_Logger
import Menu_Logger
import RUD_Entries
import Display_Work_Log

def show_entries(task, time_spent, date, comments):
    change_entry = [task, time_spent, date, comments]
    names = ['Work Task', 'Time Spent', 'Date', 'Comments'] 
    while True:
        Menu_Logger.clear()
        print(" Pay close attention if all entries are correct.... The following entries are: ")
        Display_Work_Log.print_all_entries(change_entry, names)
        print(" If want to change something that's still possible")
        confirm_entry(task, time_spent, date, comments)
        break

def confirm_entry(task, time_spent, date, comments):
    while True:
        choice = input("Do you want to a) Save or b) Edit or c) Delete entries? ")

        choices = ["a", "b", "c"]
        if choice.lower() in choices: 
            if choice.lower() == 'a':
                Delete_Save_Edit_Entries.save_entry(task, time_spent, date, comments)
                break
            elif choice.lower() == 'c' : 
                Delete_Save_Edit_Entries.delete_entry(task, time_spent, date, comments)
                break
            else: 
                Delete_Save_Edit_Entries.edit_entry(task, time_spent, date, comments)
                break
        else: 
            input("That's an invalid input. Please only enter a) Save or b) Edit or c) Delete entries. Press enter to continue...")
            continue