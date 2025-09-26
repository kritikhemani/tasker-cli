import typer
from rich.console import Console
from models import Task
# import database functions (assuming you implemented them)

app = typer.Typer(help="A simple Task Management CLI.")
console = Console()

@app.command()
def add(
    title: str,
    priority: typer.Option(3, "--priority", "-p", help="Task priority (1-5, 1 is highest)"),
    due: typer.Option(None, "--due", "-d", help="Due date (YYYY-MM-DD)")
):
    """Add a new task."""
    new_task = Task(title=title, priority=priority, due_date=due)
    # database.add_task(new_task)  <-- Call DB function
    console.print(f"[green]Task added: [bold]{title}[/bold][/green]")

@app.command()
def list():
    """List all tasks."""
    # tasks = database.get_all_tasks() <-- Call DB function
    # Use rich.Table to display tasks neatly
    console.print("Displaying tasks...")

# ... Define complete, delete commands similarly