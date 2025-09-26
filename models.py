from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class Task(BaseModel):
    # 'id' is optional for Pydantic model creation, but present in DB
    id: Optional[int] = None
    title: str = Field(min_length=3)
    priority: int = Field(default=3, ge=1, le=5) # 1=High, 5=Low
    due_date: Optional[date] = None
    status: str = Field(default="Pending")
    created_at: Optional[date] = None # Filled by the database layer