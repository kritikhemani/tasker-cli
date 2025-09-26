import sqlite3
from datetime import datetime
from typing import List, Optional
from models import Task # Assuming Task is imported from your models.py

# --- Configuration ---
DATABASE_NAME = "tasks.db"

# --- Initialization ---

def get_db_connection():
    """Returns a connection object to the SQLite database."""
    # `sqlite3.Row` allows accessing columns by name instead of index
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    """Creates the tasks table if it does not already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL to create the table based on the DESIGN.md schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority INTEGER NOT NULL,
            due_date TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Call this once at the start of the application
initialize_db()

# --- CRUD Operations ---

def add_task(task: Task) -> int:
    """Inserts a new task into the database. Returns the ID of the new task."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    now = datetime.now().isoformat(timespec='minutes')
    due_date_str = task.due_date.isoformat() if task.due_date else None

    # Insert data, using placeholders (?) to prevent SQL injection
    cursor.execute("""
        INSERT INTO tasks (title, priority, due_date, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        task.title, 
        task.priority, 
        due_date_str, 
        task.status, 
        now
    ))
    
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return task_id

def row_to_task(row: sqlite3.Row) -> Task:
    """Converts a sqlite3.Row object into a Pydantic Task model."""
    if not row:
        return None
    return Task(
        id=row['id'],
        title=row['title'],
        priority=row['priority'],
        due_date=row['due_date'],
        status=row['status'],
        created_at=row['created_at']
    )

def get_all_tasks(include_completed: bool = False) -> List[Task]:
    """Retrieves all tasks, optionally excluding completed ones."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM tasks"
    params = []
    
    if not include_completed:
        query += " WHERE status = ?"
        params.append("Pending")
        
    query += " ORDER BY priority ASC, created_at DESC"
        
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    # Use list comprehension and the conversion helper
    return [row_to_task(row) for row in rows]

def get_task_by_id(task_id: int) -> Optional[Task]:
    """Retrieves a single task by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    return row_to_task(row)

def update_task_status(task_id: int, new_status: str):
    """Updates the status of a task (e.g., 'Completed')."""
    if new_status not in ["Pending", "Completed"]:
        raise ValueError("Status must be 'Pending' or 'Completed'")
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE tasks SET status = ? WHERE id = ?
    """, (new_status, task_id))
    
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    
    if rows_affected == 0:
        raise ValueError(f"Task with ID {task_id} not found.")

def delete_task(task_id: int):
    """Deletes a task permanently from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    
    if rows_affected == 0:
        raise ValueError(f"Task with ID {task_id} not found.")