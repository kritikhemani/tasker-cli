Tasker CLI 🚀

A simple, fast, and typed command-line application for managing your daily to-do list, using SQLite for persistent storage.

Features

    ✅ Simple: Intuitive command structure.

    💾 Persistent: All data is saved reliably to an SQLite file.

    ✨ Elegant: Uses rich for beautiful, colored terminal output.

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
