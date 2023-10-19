###########################################################Create a simple task tracker###########################################################

############################################################### Defined functions ###############################################################


## Spacer ##
def spacer():
    print("-----------------------------------------")

## 1. Adding a task ##
#Confirm the user's input
def confirm_input(task):
        while True:
            spacer()
            confirm_task = input(f"You have entered:\n\n[ ] {task}\n\nDoes this look correct?\nPlease enter y/n:\n> ").lower()
            if confirm_task == 'exit':
                spacer()
                print("Deleting draft and exiting to menu...\n")
                return False
                break
            elif confirm_task == 'quit':
                spacer()
                print("Quitting program... Thank you!")
                quit()
            elif confirm_task == 'y':
                with open('Tasks.txt', 'a') as file:
                    with open('unfinished_tasks.txt', 'a') as unfinished_file:
                        file.write(f"[ ] {task}\n")
                        unfinished_file.write(f"[ ] {task}\n")
                spacer()
                print("Task successfully added to Tasks.txt\n")
                return False
                break
            elif confirm_task == 'n':
                print("Entry deleted.")
                return True
                break
            else:
                print("INVALID ENTRY")
#Add a task to the list
def add_task():
    while True: #Loop for user input
        #User input
        spacer()
        task = input("1. Create a new task\nType 'exit' to exit to menu.\nEnter task below:\n> ").lower()
        if task.lower() == 'exit':
            spacer()
            print("Exiting to menu...\n")
            break
        elif task.lower() == 'quit':
            spacer()
            print("Quitting program... Thank you!")
            quit()
        else:
            if confirm_input(task) == False:
                break
            else:
                continue

## 2. Completing a task ##
def complete_task():
    task_to_complete = input("Enter the task you would like to be marked as completed:\n").lower()
    if task_to_complete == 'quit':
        spacer()
        print("Quitting program... Thank you!")
        quit()
    elif task_to_complete == 'exit':
        spacer()
        print("Exiting to menu...\n")
        return
    try:
        with open('Tasks.txt', 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("You currently do not have any tasks saved.")
        else:
            found = False
            with open('Tasks.txt', 'w') as file:
                    with open('completed_tasks.txt', 'a') as completed_file:
                        for task in tasks:
                            if task.strip().lower() == f"[ ] {task_to_complete}":
                                found = True
                                completed_file.write(f"[X] {task_to_complete}\n")
                                print(f"Task '{task_to_complete}' marked as completed.")
                            else:
                                file.write(task)
                    if not found:
                        spacer()
                        print(f"Task '{task_to_complete}' not found.")

    except FileNotFoundError:
        print("Error: File not found. Returning to the menu.")

## 3. Deleting a task ##
def delete_task():
    if display_tasks() == False:
        return
    task_to_delete = input("Enter the task you would like deleted:\n").lower()
    if task_to_delete == 'quit':
        spacer()
        print("Quitting program... Thank you!")
        quit()
    elif task_to_delete == 'exit':
        spacer()
        print("Deletion canceled. Exiting to menu...\n")
        return
    try:
        with open('Tasks.txt', 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("You currently do not have any tasks saved.")
        else:
            found = False
            with open('Tasks.txt', 'w') as file:
                for task in tasks:
                    if task.strip().lower() == f"[ ] {task_to_delete}":
                        found = True
                        print(f"Task '{task_to_delete}' deleted.")
                    else:
                        file.write(task)
            if not found:
                spacer()
                print(f"Task '{task_to_delete}' not found.")

    except FileNotFoundError:
        print("Error: File not found. Returning to the menu.")

    
## 4, 5. Display tasks
def display_tasks():
    try:
        with open('Tasks.txt', 'r') as file:
            tasks = file.readlines()
        
        if not tasks:
            print("You currently do not have any tasks saved.")
            spacer()
        else:
            for task in tasks:
                print(task.strip())
            spacer()
    except FileNotFoundError:
        print("Error: File not found. Returning to menu.")
        return False
    
def display_completed_tasks():
    try:
        with open('completed_tasks.txt', 'r') as file:
            tasks = file.readlines()
        
        if not tasks:
            print("You currently do not have any completed tasks.")
            spacer()
        else:
            for task in tasks:
                print(task.strip())
            spacer()
    except FileNotFoundError:
        print("Error: File not found. Returning to menu.")
        return False


## Menu ##

def menu():
    print("Welcome to Task Supervisor!\n")
    while True:
        menu_selection = input(f"Please choose from the following options:\n1. Create a new task\n2. Mark a task completed\n3. Delete a previous task\n4. Display tasks\n5. Display completed tasks.\nType 'exit' at any time to return to menu.\nType 'quit' at any time to exit program.\n-----------------------------------------\n> ")
           
        if menu_selection.lower() == 'quit':
            print("Quitting program... Thank you!")
            quit()
        elif menu_selection == '1':
            add_task()
        elif menu_selection == '2':
            complete_task()
        elif menu_selection == '3':
            spacer()
            delete_task()
        elif menu_selection == '4':
            print("All Tasks:")
            display_tasks()
        elif menu_selection == '5':
            print("Completed Tasks:")
            display_completed_tasks()
        else:
            print("Invalid entry. Please select a valid option.")




        
### Code ### 

#Display menu
menu()