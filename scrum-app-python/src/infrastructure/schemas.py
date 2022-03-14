from typing import Optional
from pydantic import BaseModel


class TaskBase(BaseModel):    
    title: Optional[str]
    description:Optional[str]
    color:Optional[str]
    status:Optional[str]


class TaskCreate(TaskBase):
    title: str
    scrum_id: Optional[int]


class Task(TaskBase):
    id: int    
    scrum_id: int

    class Config:
        orm_mode = True 

class TaskBase(BaseModel):
    title: str


class ScrumCreate(TaskBase):
    title: str


class Scrum(TaskBase):
    id: Optional[int]
    tasks: Optional[list[Task]] = []

    class Config:
        orm_mode = True

