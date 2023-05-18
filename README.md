![Header](banner.png)
<p align="center">
  <img src="https://img.shields.io/aur/last-modified/google-chrome" />
  <img src="https://img.shields.io/amo/stars/dustman" />
  <img src="https://img.shields.io/github/stars/Chamepp/Daily.py?style=social" />
  <img src="https://img.shields.io/amo/users/dustman" />
</p>


# Daily.py Documentation

## Introduction
Welcome to the documentation for Daily.py! This repository provides a simple and lightweight Python package that helps you manage daily tasks and routines efficiently. With Daily.py, you can create, update, and track your daily tasks effortlessly.

## Installation
To use Daily.py in your Python project, you need to install it first. Follow the steps below to install the package:

1. Open a terminal or command prompt.
2. Ensure that you have Python 3 installed on your system.
3. Run the following command to install Daily.py using pip:
   ```
   pip install daily.py
   ```

## Getting Started
Once you have installed Daily.py, you can import it into your Python code using the following import statement:

```python
from daily import Daily
```

To start using Daily.py, you need to create an instance of the `Daily` class:

```python
daily = Daily()
```

## Basic Usage

### Creating a Task
You can create a task using the `create_task` method. The method takes two parameters: the task name and an optional description. It returns the unique ID assigned to the task.

```python
task_id = daily.create_task("Finish report", "Write the final report for the project")
```

### Updating a Task
You can update a task by providing its ID and the new task details using the `update_task` method. The method takes three parameters: the task ID, the new task name, and an optional new description.

```python
daily.update_task(task_id, "Submit report", "Submit the final report to the supervisor")
```

### Marking a Task as Completed
You can mark a task as completed using the `complete_task` method. It takes the task ID as a parameter.

```python
daily.complete_task(task_id)
```

### Deleting a Task
You can delete a task using the `delete_task` method. It takes the task ID as a parameter.

```python
daily.delete_task(task_id)
```

### Listing All Tasks
You can retrieve a list of all tasks using the `get_all_tasks` method. It returns a list of dictionaries, where each dictionary represents a task with its ID, name, description, and status (completed or not).

```python
tasks = daily.get_all_tasks()
for task in tasks:
    print(task)
```

## Advanced Features

### Custom Task Status
You can define custom task statuses by using the `set_task_status` method. It allows you to set the status for a particular task ID.

```python
daily.set_task_status(task_id, "In Progress")
```

### Task Prioritization
You can assign priorities to tasks using the `set_task_priority` method. It takes the task ID and priority level as parameters.

```python
daily.set_task_priority(task_id, 2)
```

### Task Reminders
You can set reminders for tasks using the `set_task_reminder` method. It takes the task ID and a reminder time in the format `HH:MM` (24-hour format) as parameters.

```python
daily.set_task_reminder(task_id, "09:00")
```

## Conclusion
Congratulations! You have learned the basics of using Daily.py to manage your daily tasks efficiently. Feel free to explore the various methods and features provided by the package to customize your task management system. For further details, refer to the source code and the official Daily.py repository on [GitHub](https://github.com/Chamepp/Daily.py).
