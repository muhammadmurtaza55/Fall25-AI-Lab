def show_menu():
    print(" TO-DO LIST MENU ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("You don’t have any tasks yet")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your list.")

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the number of the task you want to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter the updated task: ")
                old_task = tasks[num - 1]
                tasks[num - 1] = new_task
                print(f"Task updated: '{old_task}' → '{new_task}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the number of the task you want to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to your To-Do List!")
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nExiting  Goodbye!")
            break
        else:
            print("That’s not a valid option, please try again.")

if __name__ == "__main__":
    main()
