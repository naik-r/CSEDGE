class Task:

  def __init__(self, description):
    self.description = description
    self.completed = False

  def mark_completed(self):
    self.completed = True

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"- [{status}] {self.description}"

class ToDoList:

  def __init__(self):
    self.tasks = []

  def add_task(self, description):
 
    self.tasks.append(Task(description))

  def delete_task(self, index):

    if 0 <= index < len(self.tasks):
      del self.tasks[index]
    else:
      print("Invalid task index.")

  def mark_task_completed(self, index):

    if 0 <= index < len(self.tasks):
      self.tasks[index].mark_completed()
    else:
      print("Invalid task index.")

  def list_tasks(self):

    if not self.tasks:
      print("No tasks in the list.")
    else:
      for i, task in enumerate(self.tasks):
        print(f"{i+1}. {task}")

  def main_loop(self):

    while True:
      print("\nTo-Do List")
      print("1. Add Task")
      print("2. Delete Task")
      print("3. Mark Task Completed")
      print("4. List Tasks")
      print("5. Exit")
      choice = input("Enter your choice: ")

      if choice == '1':
        description = input("Enter task description: ")
        self.add_task(description)
      elif choice == '2':
        self.list_tasks()
        index = int(input("Enter the index of the task to delete: ")) - 1
        self.delete_task(index)
      elif choice == '3':
        self.list_tasks()
        index = int(input("Enter the index of the task to mark completed: ")) - 1
        self.mark_task_completed(index)
      elif choice == '4':
        self.list_tasks()
      elif choice == '5':
        break
      else:
        print("Invalid choice.")

if __name__ == "__main__":
  todo_list = ToDoList()
  todo_list.main_loop()
