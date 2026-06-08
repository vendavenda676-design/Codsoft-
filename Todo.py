tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added")

    elif choice == '2':
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == '3':
        num = int(input("Enter task number to remove: "))
        tasks.pop(num - 1)
        print("Task Removed")

    elif choice == '4':
        print("Exit")
        break

    else:
        print("Invalid Choice")