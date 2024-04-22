#project: Task manager with reminder system and some additional faeture with python and its a console base project

import datetime

# Function to add a new task
def add_task(tasks):
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High, Medium, Low): ")
    status = "Pending"
    tasks.append({
        'task_name': task_name,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'status': status
    })
    print("Task added successfully!")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"Task {index}:")
            print(f"Name: {task['task_name']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print("-" * 20)

# Function to set a reminder for upcoming tasks
def set_reminder(tasks):
    today = datetime.date.today()
    upcoming_tasks = [task for task in tasks if datetime.datetime.strptime(task['due_date'], "%Y-%m-%d").date() > today]
    if not upcoming_tasks:
        print("No upcoming tasks found.")
    else:
        print("Upcoming Tasks:")
        for task in upcoming_tasks:
            print(f"Task: {task['task_name']}")
            print(f"Due Date: {task['due_date']}")
            print("-" * 20)
        print("Reminder set successfully!")

# Main function
def main():
    tasks = []
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Set Reminder")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            set_reminder(tasks)
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
