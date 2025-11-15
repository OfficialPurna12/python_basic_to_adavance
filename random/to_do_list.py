todo_list = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    # View Tasks
    if choice == "1":
        if len(todo_list) == 0:
            print("\nNo tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    # Add Task
    elif choice == "2":
        task = input("Enter new task: ")
        todo_list.append(task)
        print(f"✅ '{task}' added to your list.")

    # Delete Task
    elif choice == "3":
        if len(todo_list) == 0:
            print("\nNo tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                if 0 < task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"❌ '{removed}' removed from your list.")
                else:
                    print("Invalid number! Please try again.")
            except ValueError:
                print("⚠️ Please enter a valid number!")

    # Exit Program
    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 4.")


