from datetime import datetime
import json
import os
from typing import List, Dict
from dataclasses import dataclass
import uuid

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# ASCII art for header
HEADER = f"""
{RED}╔════════════════════════════════════╗{RESET}
{RED}║      {YELLOW}TASK MANAGER CLI{RESET}      {RED}║{RESET}
{RED}╚════════════════════════════════════╝{RESET}
"""

@dataclass
class Task:
    id: str
    title: str
    description: str
    priority: str
    due_date: str
    category: str
    completed: bool
    created_at: str

def load_tasks() -> List[Task]:
    try:
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                task_data = json.load(f)
                return [Task(**data) for data in task_data]
    except Exception as e:
        print(f"{RED}Error loading tasks: {e}{RESET}")
    return []

def save_tasks(tasks: List[Task]):
    try:
        with open("tasks.json", "w") as f:
            json.dump([vars(task) for task in tasks], f, indent=2)
    except Exception as e:
        print(f"{RED}Error saving tasks: {e}{RESET}")

def display_tasks(tasks: List[Task]):
    if not tasks:
        print(f"{YELLOW}No tasks available.{RESET}")
        return
    print(f"{BLUE}┌{'─' * 60}┐{RESET}")
    for task in tasks:
        status = f"{GREEN}✓{RESET}" if task.completed else " "
        print(f"{BLUE}│ [{status}] {task.title[:20]:<20} | {task.priority[:10]:<10} | {task.due_date[:10]:<10} | {task.category[:10]:<10} | ID: {task.id} │{RESET}")
    print(f"{BLUE}└{'─' * 60}┘{RESET}")

def add_task(tasks: List[Task]):
    print(f"{GREEN}Selected: Add Task{RESET}")
    task_data = {
        "id": str(uuid.uuid4()),
        "title": input(f"{YELLOW}Enter task title: {RESET}"),
        "description": input(f"{YELLOW}Enter description: {RESET}"),
        "priority": input(f"{YELLOW}Enter priority (low/medium/high): {RESET}"),
        "due_date": input(f"{YELLOW}Enter due date (YYYY-MM-DD): {RESET}"),
        "category": input(f"{YELLOW}Enter category: {RESET}"),
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(Task(**task_data))
    save_tasks(tasks)
    print(f"{GREEN}Task created successfully!{RESET}")

def edit_task(tasks: List[Task]):
    print(f"{GREEN}Selected: Edit Task{RESET}")
    display_tasks(tasks)
    task_id = input(f"{YELLOW}Enter task ID to edit: {RESET}")
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        task.title = input(f"{YELLOW}Enter new title ({task.title}): {RESET}") or task.title
        task.description = input(f"{YELLOW}Enter new description ({task.description}): {RESET}") or task.description
        task.priority = input(f"{YELLOW}Enter new priority ({task.priority}): {RESET}") or task.priority
        task.due_date = input(f"{YELLOW}Enter new due date ({task.due_date}): {RESET}") or task.due_date
        task.category = input(f"{YELLOW}Enter new category ({task.category}): {RESET}") or task.category
        save_tasks(tasks)
        print(f"{GREEN}Task updated successfully!{RESET}")
    else:
        print(f"{RED}Task not found.{RESET}")

def delete_task(tasks: List[Task]):
    print(f"{GREEN}Selected: Delete Task{RESET}")
    display_tasks(tasks)
    task_id = input(f"{YELLOW}Enter task ID to delete: {RESET}")
    task_to_delete = next((t for t in tasks if t.id == task_id), None)
    if task_to_delete:
        print(f"{YELLOW}Deleting task with ID: {task_id}{RESET}")
        tasks[:] = [t for t in tasks if t.id != task_id]
        save_tasks(tasks)
        print(f"{GREEN}Task deleted successfully!{RESET}")
    else:
        print(f"{RED}Task not found.{RESET}")

def toggle_complete(tasks: List[Task]):
    print(f"{GREEN}Selected: Toggle Completion{RESET}")
    display_tasks(tasks)
    task_id = input(f"{YELLOW}Enter task ID to toggle completion: {RESET}")
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        task.completed = not task.completed
        save_tasks(tasks)
        print(f"{GREEN}Task completion toggled!{RESET}")
    else:
        print(f"{RED}Task not found.{RESET}")

def filter_tasks(tasks: List[Task]):
    print(f"{GREEN}Selected: Filter Tasks{RESET}")
    category = input(f"{YELLOW}Enter category to filter by: {RESET}")
    filtered_tasks = [t for t in tasks if category.lower() in t.category.lower()]
    display_tasks(filtered_tasks)
    input(f"{YELLOW}Press Enter to continue...{RESET}")

def sort_tasks(tasks: List[Task]):
    print(f"{GREEN}Selected: Sort Tasks{RESET}")
    sort_by = input(f"{YELLOW}Sort by (priority/created_at): {RESET}").lower()
    if sort_by == "priority":
        priority_order = {"high": 0, "medium": 1, "low": 2}
        tasks.sort(key=lambda t: priority_order.get(t.priority.lower(), 3))
    else:
        tasks.sort(key=lambda t: t.created_at)
    save_tasks(tasks)
    display_tasks(tasks)
    input(f"{YELLOW}Press Enter to continue...{RESET}")

def main():
    tasks = load_tasks()
    while True:
        print(HEADER)
        print(f"{BLUE}1. Add Task{RESET}")
        print(f"{BLUE}2. Edit Task{RESET}")
        print(f"{BLUE}3. Delete Task{RESET}")
        print(f"{BLUE}4. Toggle Completion{RESET}")
        print(f"{BLUE}5. Filter Tasks{RESET}")
        print(f"{BLUE}6. Sort Tasks{RESET}")
        print(f"{BLUE}7. Display All Tasks{RESET}")
        print(f"{BLUE}8. Exit{RESET}")
        choice = input(f"{YELLOW}Enter your choice (1-8): {RESET}")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            toggle_complete(tasks)
        elif choice == "5":
            filter_tasks(tasks)
        elif choice == "6":
            sort_tasks(tasks)
        elif choice == "7":
            print(f"{GREEN}Selected: Display All Tasks{RESET}")
            display_tasks(tasks)
            input(f"{YELLOW}Press Enter to continue...{RESET}")
        elif choice == "8":
            print(f"{GREEN}Selected: Exit{RESET}")
            print(f"{YELLOW}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()