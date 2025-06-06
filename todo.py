#!/usr/bin/env python3
import json
from pathlib import Path
import argparse

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

DATA_FILE = Path("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    header = f"{BOLD}{CYAN}*** To-Do List ***{RESET}"
    print(header)
    for i, task in enumerate(tasks, 1):
        if task["done"]:
            status = f"{GREEN}[x]{RESET}"
            desc = f"{GREEN}{task['description']}{RESET}"
        else:
            status = f"{YELLOW}[ ]{RESET}"
            desc = task["description"]
        print(f"{i}. {status} {desc}")


def done_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"{GREEN}Task {index} marked as done.{RESET}")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"{CYAN}Task {index} deleted.{RESET}")




def build_parser():
    parser = argparse.ArgumentParser(description="Command line to-do list")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("description", nargs="+", help="Task description")

    sub.add_parser("list", help="List tasks")

    p_done = sub.add_parser("done", help="Mark task as done")
    p_done.add_argument("index", type=int, help="Task number")

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("index", type=int, help="Task number")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        add_task(" ".join(args.description))
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        done_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)


if __name__ == "__main__":
    main()
