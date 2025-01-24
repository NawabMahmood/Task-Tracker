Task Tracker CLI

A simple command-line interface (CLI) tool to help you track and manage your tasks efficiently. This project allows you to add, update, delete, and list tasks, as well as mark them as in progress or completed. Tasks are stored in a JSON file for persistence.

Features

Add Tasks: Create new tasks with a description.

Update Tasks: Modify existing tasks by their unique ID.

Delete Tasks: Remove tasks by their unique ID.

List Tasks:

All tasks

Tasks filtered by status (todo, in-progress, done)

Mark Tasks:

Mark tasks as in-progress.

Mark tasks as done.

Installation

Clone the repository:

git clone <repository_url>
cd Task-Tracker

Make the script executable:

chmod +x task-cli.py

(Optional) Add the script to your PATH for global access:

mv task-cli.py /usr/local/bin/task-cli

Usage

General Syntax

./task-cli.py <command> [options]

Or, if you added it to your PATH:

task-cli <command> [options]

Commands

1. Add a Task

task-cli add "<task_description>"

Adds a new task to your task list.

Example:

task-cli add "Buy groceries"

2. Update a Task

task-cli update <task_id> "<new_description>"

Updates the description of an existing task.

Example:

task-cli update 1 "Buy groceries and cook dinner"

3. Delete a Task

task-cli delete <task_id>

Deletes a task by its unique ID.

Example:

task-cli delete 1

4. List All Tasks

task-cli list

Displays all tasks.

Example:

task-cli list

5. List Tasks by Status

task-cli list <status>

Filters tasks by status (todo, in-progress, done).

Example:

task-cli list done

6. Mark a Task as In Progress

task-cli mark-in-progress <task_id>

Marks a task as in-progress.

Example:

task-cli mark-in-progress 2

7. Mark a Task as Done

task-cli mark-done <task_id>

Marks a task as done.

Example:

task-cli mark-done 2

File Structure

Task-Tracker/
│
├── task-cli.py         # Entry point for the CLI application
├── task_manager.py     # Handles task operations (add, update, delete, etc.)
├── tasks.json          # Stores all task data in JSON format
└── README.md           # Documentation for the project

Task Data Structure

Tasks are stored in tasks.json with the following properties:

{
  "tasks": [
    {
      "id": 1,
      "description": "Buy groceries",
      "status": "todo",
      "createdAt": "2025-01-23T10:00:00",
      "updatedAt": "2025-01-23T10:00:00"
    }
  ]
}

id: Unique identifier for the task.

description: A short description of the task.

status: Task status (todo, in-progress, done).

createdAt: Timestamp of when the task was created.

updatedAt: Timestamp of the last update.