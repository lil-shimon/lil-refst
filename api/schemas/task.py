from typing import Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="歯磨きをする")
    done: bool = Field(False, description="完了したか")
