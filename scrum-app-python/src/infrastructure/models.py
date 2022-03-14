from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Scrum(Base):
    __tablename__ = 'scrum'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256))

    tasks = relationship("Task", back_populates="task")

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(String)
    color  = Column(String(256))
    status = Column(String)

    scrum_id = Column(Integer, ForeignKey("scrum.id"))
    task = relationship("Scrum", back_populates="tasks")