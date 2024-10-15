import json
import os


# The Task class holds all the information for each task.
# We're keeping it simple: just an ID, title, and whether it's done or not.
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id  # Unique identifier for each task
        self.title = title  # What the task is about
        self.completed = completed  # Whether the task is done or not

    def __repr__(self):
        # This method is useful for printing the task info in a readable format
        status = "Completed" if self.completed else "Not Completed"
        return f"Task({self.id}, '{self.title}', {status})"


# The main list where we'll keep all the tasks in memory
tasks = []
# Name of the file where we'll save the tasks (in JSON format)
task_file = 'tasks.json'


# Function to add a new task to the list
def add_task(title):
    task_id = len(tasks) + 1  # Automatically assign an ID based on the number of tasks
    task = Task(task_id, title)  # Create a new Task object
    tasks.append(task)  # Add the task to our list
    print(f"Task '{title}' added with ID {task_id}.")


# Function to display all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Here are your tasks:")
        for task in tasks:
            print(task)


# Function to delete a task based on its ID
def delete_task(task_id):
    global tasks  # Since we're modifying the list, we declare it as global
    tasks = [task for task in tasks if task.id != task_id]  # Filter out the task by its ID
    print(f"Task {task_id} deleted.")


# Function to mark a task as completed
def mark_task_completed(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True  # Set the task's completed status to True
            print(f"Task {task_id} marked as completed.")
            break
    else:
        print(f"No task found with ID {task_id}.")


# Save the current list of tasks to a file
def save_tasks():
    with open(task_file, 'w') as f:
        json_tasks = [task.__dict__ for task in tasks]  # Convert each task to a dictionary
        json.dump(json_tasks, f)  # Write the list of dictionaries to the file
    print("Tasks saved to file.")


# Load tasks from the file when the program starts
def load_tasks():
    if os.path.exists(task_file):  # Only load if the file exists
        with open(task_file, 'r') as f:
            loaded_tasks = json.load(f)  # Load tasks from JSON file
            for task_data in loaded_tasks:
                # Recreate Task objects from the loaded data
                task = Task(task_data['id'], task_data['title'], task_data['completed'])
                tasks.append(task)  # Add to the list
        print("Tasks loaded from file.")


# Main program loop - this is where the user interacts with the CLI
def main():
    load_tasks()  # Load saved tasks when the program starts

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Save and Exit")

        # Get the user's choice and handle it
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_task_completed(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# This block ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
