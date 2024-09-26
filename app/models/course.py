from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Recommendation(BaseModel):
    professor_id: Optional[str] = None
    student_id: Optional[str] = None
    completed: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "professor_id": "1",
                "student_id": "1",
                "completed": "yes",
            }
        }
