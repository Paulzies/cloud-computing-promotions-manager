from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Promotion(BaseModel):
    promotion_id: Optional[str] = None
    description: Optional[str] = None
    sku: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "promotion_id": "p1",
                "description": "sample description",
                "SKU": "s1",
                "start_date": "2024-01-01",
                "end_date": "2024-12-31",
            }
        }
