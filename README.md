# 📚 README.md (Documentation)

## Tasker CLI 🚀

A simple, fast, and typed command-line application for managing your daily to-do list, using SQLite for persistent storage.

## ✨ Features

    ✅ Typed CLI: Uses Python type hints (via Typer and Pydantic) for robust command arguments and data models.

    💾 Persistent Storage: Tasks are reliably saved to a single tasks.db file using SQLite.

    ✅ Rich Output: Beautiful, readable terminal output powered by the rich library.

    💾 Core CRUD: Easily Create, Read (List), Update (Complete), and Delete tasks.



    

## Installation

    Clone the Repository:
    Bash

git clone https://github.com/YOUR_USERNAME/tasker-cli.git
cd tasker-cli

## Setup Environment:
Bash

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    (Note: You would need to create a requirements.txt listing typer, pydantic, rich)

## Usage

The main command is tasker. Run with --help for details:
Bash

python tasker.py --help

## Examples

Action	Command
Add a high-priority task	python tasker.py add "Finish Tasker CLI" -p 1
List all tasks	python tasker.py list
Complete task ID 5	python tasker.py complete 5


## 🌐 Publishing to GitHub (Explanation)

To make your project available to the world and manage its versions, follow these steps:

1. Initialize Git Repository Locally

    Initialize Git: In your project root (tasker_cli folder):
    Bash

git init

Create .gitignore: This file tells Git which files to ignore (like the virtual environment and the database file).

# .gitignore content
venv/
__pycache__/
*.pyc
tasks.db

Add all files: Stage all your project files (tasker.py, database.py, models.py, README.md, DESIGN.md, .gitignore).
Bash

git add .

Commit the initial version:
Bash

    git commit -m "Initial commit: tasker cli with sqlite storage"

2. Create Repository on GitHub

    Go to GitHub.com and log in.

    Click the + icon in the top right and select "New repository."

    Name it tasker-cli (or similar). Do not check the option to add a README, license, or .gitignore (since you already created them locally).

    Click "Create repository."

3. Link Local to Remote

GitHub will show you commands to link your local repository to the new remote one.

    Set the remote origin: Copy the URL (e.g., https://github.com/YOUR_USERNAME/tasker-cli.git).
    Bash

git remote add origin YOUR_REPO_URL

Push the code: Push your master/main branch to GitHub.
Bash

    git push -u origin main
    # Use 'master' instead of 'main' if your local branch is named 'master'


