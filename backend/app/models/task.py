from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "title": "Task Title",
                "description": "Task Description"
            }
        }