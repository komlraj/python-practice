def display_menu():
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n=== Tasks ===")
        for task in tasks:
            print(f"{task['id']} - {task['title']} - {'Complete' if task['completed'] else 'Incomplete'}")
            
def add_task(tasks):
    title = input("Enter the task: ")
    tasks.append({"id": len(tasks) + 1, "title": title, "completed": False})
    print(f"Task '{title}' added.")
    
def mark_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['title']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
