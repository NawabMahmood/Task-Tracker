#!/usr/bin/env python3

import sys
from task_manager import TaskManager

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return
    
    command = sys.argv[1]
    args = sys.argv[2:]
    manager = TaskManager()

    if command == "add":
        if len(args) < 1:
            print("Usage: task-cli add <task_description>")
        else:
            manager.add_task(args[0])
    elif command == "list":
        status = args[0] if args else None
        manager.list_tasks(status)
    elif command == "update":
        if len(args) < 2:
            print("Usage: task-cli update <task_id> <new_description>")
        else:
            manager.update_task(int(args[0]), args[1])
    elif command == "delete":
        if len(args) < 1:
            print("Usage: task-cli delete <task_id>")
        else:
            manager.delete_task(int(args[0]))
    elif command == "mark-in-progress":
        if len(args) < 1:
            print("Usage: task-cli mark-in-progress <task_id>")
        else:
            manager.mark_task_status(int(args[0]), "in-progress")
    elif command == "mark-done":
        if len(args) < 1:
            print("Usage: task-cli mark-done <task_id>")
        else:
            manager.mark_task_status(int(args[0]), "done")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
