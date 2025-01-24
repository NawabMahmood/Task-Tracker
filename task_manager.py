import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

class TaskManager:
    def __init__(self):
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w") as file:
                json.dump({"tasks": []}, file)

    def _load_tasks(self):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    def _save_tasks(self, data):
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def add_task(self, description):
        data = self._load_tasks()
        task_id = max([task["id"] for task in data["tasks"]] or [0]) + 1
        new_task = {
            "id": task_id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        data["tasks"].append(new_task)
        self._save_tasks(data)
        print(f"Task added successfully (ID: {task_id})")

    def list_tasks(self, status=None):
        data = self._load_tasks()
        tasks = data["tasks"]
        if status:
            tasks = [task for task in tasks if task["status"] == status]
        for task in tasks:
            print(f"[{task['id']}] {task['description']} - {task['status']}")

    def update_task(self, task_id, new_description):
        data = self._load_tasks()
        for task in data["tasks"]:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = datetime.now().isoformat()
                self._save_tasks(data)
                print(f"Task {task_id} updated successfully")
                return
        print(f"Task {task_id} not found")

    def delete_task(self, task_id):
        data = self._load_tasks()
        tasks = [task for task in data["tasks"] if task["id"] != task_id]
        if len(tasks) == len(data["tasks"]):
            print(f"Task {task_id} not found")
            return
        data["tasks"] = tasks
        self._save_tasks(data)
        print(f"Task {task_id} deleted successfully")

    def mark_task_status(self, task_id, status):
        data = self._load_tasks()
        for task in data["tasks"]:
            if task["id"] == task_id:
                task["status"] = status
                task["updatedAt"] = datetime.now().isoformat()
                self._save_tasks(data)
                print(f"Task {task_id} marked as {status}")
                return
        print(f"Task {task_id} not found")
