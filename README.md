# 📚 README.md (Documentation)

## Tasker CLI 🚀

A simple, fast, and typed command-line application for managing your daily to-do list, using SQLite for persistent storage.

## ✨ Features

    ✅ Typed CLI: Uses Python type hints (via Typer and Pydantic) for robust command arguments and data models.

    💾 Persistent Storage: Tasks are reliably saved to a single tasks.db file using SQLite.

    ✅ Rich Output: Beautiful, readable terminal output powered by the rich library.

    💾 Core CRUD: Easily Create, Read (List), Update (Complete), and Delete tasks.



    

Installation

    Clone the Repository:
    Bash

git clone https://github.com/YOUR_USERNAME/tasker-cli.git
cd tasker-cli

Setup Environment:
Bash

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    (Note: You would need to create a requirements.txt listing typer, pydantic, rich)

Usage

The main command is tasker. Run with --help for details:
Bash

python tasker.py --help

Examples

Action	Command
Add a high-priority task	python tasker.py add "Finish Tasker CLI" -p 1
List all tasks	python tasker.py list
Complete task ID 5	python tasker.py complete 5
