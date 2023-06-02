import datetime

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]


# Create some tasks
task1 = Task("Complete report", datetime.date(2023, 5, 31))
task2 = Task("Prepare presentation", datetime.date(2023, 6, 5))
task3 = Task("Review code", datetime.date(2023, 6, 10))

# Create a project and add tasks
project = Project("Software Development Project")
project.add_task(task1)
project.add_task(task2)
project.add_task(task3)

# Mark a task as completed
task1.mark_as_completed()

# Print incomplete tasks
print("Incomplete tasks:")
incomplete_tasks = project.get_incomplete_tasks()
for task in incomplete_tasks:
    print(f"- {task.title} (Due: {task.due_date})")

# Print completed tasks
print("\nCompleted tasks:")
completed_tasks = project.get_completed_tasks()
for task in completed_tasks:
    print(f"- {task.title}")

