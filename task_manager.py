import json


# Define Task Structure
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id  # Initialize the task ID
        self.title = title  # Initialize the task title
        self.completed = completed  # Initialize the completion status (default is False)

    def __repr__(self):
        # Define how to represent the Task object as a string
        return f"Task({self.id}, '{self.title}', {self.completed})"


# Implement Task Management Functions
tasks = []  # Initialize an empty list to store tasks

def add_task(title):  # Function to add a new task
    task_id = len(tasks) + 1  # Assign a new ID based on the current number of tasks
    task = Task(task_id, title)  # Create a new Task object
    tasks.append(task)  # Add the new task to the list
    print(f"Task '{title}' added.")  # Confirm the task has been added

def view_tasks():  # Function to view all tasks
    if not tasks:  # Check if there are no tasks
        print("No tasks available.")  # Inform the user
    for task in tasks:  # Iterate through each task
        status = "Completed" if task.completed else "Pending"  # Determine task status
        print(f"{task.id}. {task.title} - {status}")  # Print task ID, title, and status

def delete_task(task_id):  # Function to delete a task by ID
    global tasks  # Declare the global tasks list
    tasks = [task for task in tasks if task.id != task_id]  # Filter out the task to be deleted
    print(f"Task {task_id} deleted.")  # Confirm the task has been deleted

def mark_task_complete(task_id):  # Function to mark a task as completed
    for task in tasks:  # Iterate through each task
        if task.id == task_id:  # Check if the task ID matches
            task.completed = True  # Mark the task as completed
            print(f"Task {task_id} marked as completed.")  # Confirm the change

# File Handling
def save_tasks(filename='tasks.json'):  # Function to save tasks to a file
    with open(filename, 'w') as file:  # Open the file in write mode
        json.dump([task.__dict__ for task in tasks], file)  # Convert tasks to a dictionary and save as JSON
    print("Tasks saved to file.")  # Confirm that tasks have been saved

def load_tasks(filename='tasks.json'):  # Function to load tasks from a file
    global tasks  # Declare the global tasks list
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            tasks_data = json.load(file)  # Load the JSON data from the file
            tasks = [Task(**data) for data in tasks_data]  # Create Task objects from the loaded data
    except FileNotFoundError:  # Handle the case where the file does not exist
        print("No saved tasks found.")  # Inform the user


# Create a Command-Line Interface
def cli():  # Function for the command-line interface
    load_tasks()  # Load tasks at the start of the interface
    while True:  # Infinite loop for user interaction
        print("\nTask Manager")  # Display the task manager title
        print("1. Add Task")  # Option to add a task
        print("2. View Tasks")  # Option to view tasks
        print("3. Delete Task")  # Option to delete a task
        print("4. Mark Task as Complete")  # Option to mark a task as complete
        print("5. Save and Exit")  # Option to save tasks and exit
        choice = input("Enter your choice: ")  # Prompt the user for input

        if choice == '1':  # If the user chooses to add a task
            title = input("Enter task title: ")  # Prompt for task title
            add_task(title)  # Call the add_task function
        elif choice == '2':  # If the user chooses to view tasks
            view_tasks()  # Call the view_tasks function
        elif choice == '3':  # If the user chooses to delete a task
            task_id = int(input("Enter task ID to delete: "))  # Prompt for task ID to delete
            delete_task(task_id)  # Call the delete_task function
        elif choice == '4':  # If the user chooses to mark a task as complete
            task_id = int(input("Enter task ID to mark complete: "))  # Prompt for task ID
            mark_task_complete(task_id)  # Call the mark_task_complete function
        elif choice == '5':  # If the user chooses to save and exit
            save_tasks()  # Call the save_tasks function
            break  # Exit the loop
        else:  # If the user enters an invalid choice
            print("Invalid choice. Try again.")  # Inform the user

# Start the CLI
if __name__ == "__main__":  # Check if this script is being run directly
    cli()  # Start the command-line interface
