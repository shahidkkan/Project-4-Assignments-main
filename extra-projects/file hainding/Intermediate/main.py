# 📝 Task 2: Task Manager
# 📌 Task Manager
# 1. Add Task
# 2. View Tasks
# 3. Delete All Tasks
# 4. Exit
task_file = "tasks.txt"
def add_Task():
    tasks = input("Enter a new task: \n")
    with open(task_file,"a") as file:
        file.write(tasks + "\n")
        print("✅ Task added successfully!")
        
def View_Tasks():
    try:
         with open(task_file,"r") as file:
             tasks = file.readlines()
             if not tasks:
                   print("📂 No tasks found.")
             else:
                 print("Your Tasks 📃")
                 for index,task in enumerate(tasks,start=1):
                   print(f"{index}. {task.strip()}")
                   
    except FileNotFoundError:
        print("file Not Exits ")
        
def delete_tasks():
    with open(task_file,"w") as file:
        pass
    print("🗑️ All tasks deleted!")

while True:
    print("""
📌 Task Manager
  1. Add Task
  2. View Tasks
  3. Delete All Tasks
  4. Exit
          """)
    choice = input("Enter The Number: ")
    if choice == "1":
        add_Task()
    elif choice == "2":
        View_Tasks()
    elif choice == "3":
        delete_tasks()
    elif choice == "4":
        break