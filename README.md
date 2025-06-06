# Trending

This repository contains a simple command line to-do list application written in
 Python. The interface now uses colored terminal output for a cleaner look.

## Requirements

* Python 3.7 or later

## Usage

Add a task:

```bash
python todo.py add "Buy milk"
```

List tasks (completed tasks appear in green):

```bash
python todo.py list
```

Mark a task as done (using its number from the list):

```bash
python todo.py done 1
```

Delete a task:

```bash
python todo.py delete 1
```

Tasks are stored in `tasks.json` in the repository directory.
