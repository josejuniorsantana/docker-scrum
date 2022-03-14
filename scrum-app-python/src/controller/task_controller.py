from typing import List
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi import Query
from infrastructure import models, schemas
from service import task_service
from sqlalchemy.orm import Session

from infrastructure.database import SessionLocal, engine

from typing import Optional
from fastapi.responses import JSONResponse

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        pass
#        db.close()        
def close_db(db):
    db.close()

def get_db_self_close():
    db = SessionLocal()
    try:
        yield db
    finally:
        pass
#        db.close()           

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", description="View a list of all tasks", response_model=List[schemas.Task])
async def read_root():
    db = get_db_self_close()    
    return task_service.TaskService.get_all(db)    

@router.get("/{id}", description="Find a task info by its id", response_model=schemas.Task)
async def read_item(id: int):
    db = get_db_self_close()    
    return task_service.TaskService.get_task_by_id(db, id)    


@router.get("", description="Find a task  info by its title", response_model=schemas.Task)
async def read_item(title: str):
    return {"id": title, "name": "Mobile", "code": "M12", "price": 200.0}


@router.post("/", description="Save new task", response_model=schemas.Task)
async def add_item(task: schemas.Task, db: Session = Depends(get_db)):

    db = get_db()
    sc = task_service.TaskService.create_task(db, task=task)
    close_db(db)
    return sc


@router.put("/{id}", description="Update a task with specific id", response_model=schemas.Task)
async def update_item(id: int, task: schemas.Task):
    db = get_db_self_close()
    sc1 = task_service.TaskService.update_task(db, id, task)
    return sc1


@router.delete("/{id}", description="Delete Task with specific id")
async def delete_item(task_id: int):
    db = get_db_self_close()
    task_service.TaskService.delete_task(db, task_id)
    return 'Ok'
   