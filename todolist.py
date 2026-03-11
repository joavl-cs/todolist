# to do list 

to_do_list = []

while True:
    #task menu options 
    print("Options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # adding a task to the list
    if choice == "1":
        task = input("Enter a task to add: ")
        to_do_list.append(task)
        print(f"Task '{task}' added.")
    
    # viewing the tasks in the list
    elif choice == "2":
        if to_do_list:
            print("\nYour To-Do List:")
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")
     
    # removing a task from the list
    elif choice == "3":
        if to_do_list:
            try:
                task_num = int(input("Enter the number of the task to remove: "))
                if 1 <= task_num <= len(to_do_list):
                    removed_task = to_do_list.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to remove.")

    # exiting the program
    elif choice == "4":
        print("Goodbye!")
        break

    # handling invalid options
    else:
        print("Invalid option. Please choose again.")