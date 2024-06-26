import json

# Function to load tasks from file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

# Function to display menu
def display_menu():
    print("TO-DO LIST")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Mark Task as Undone")
    print("5. Remove Task")
    print("6. Save and Quit")

# Function to view tasks
def view_tasks(tasks):
    print("YOUR TASKS")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            status = "[X]" if task['done'] else "[ ]"
            print(f"{index}. {status} {task['task']}")
    else:
        print("No tasks found.")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully.")

# Function to mark task as done or undone
def mark_task(tasks, done=True):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number: ")) - 1
        tasks[index]['done'] = done
        print("Task marked successfully.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        del tasks[index]
        print("Task removed successfully.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main function
def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            mark_task(tasks, done=False)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            save_tasks(tasks, filename)
            print("Tasks saved. Quitting.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
