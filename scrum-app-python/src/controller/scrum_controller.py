#from msilib import schema
from typing import List
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi import Query
#from src.models.user import UserModel
from infrastructure import models, schemas
from service import scrum_service
from sqlalchemy.orm import Session

from infrastructure.database import SessionLocal, engine

from typing import Optional
from fastapi.responses import JSONResponse


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        pass
#        db.close()        
def close_db(db):
    db.close()

router = APIRouter(
    prefix="/scrums",
    tags=["Scrum"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", description="View a list of all Scrum boards", response_model=List[schemas.Scrum])
async def read_root():
    db = get_db()    
    return scrum_service.ScrumService.get_all(db)    


@router.get("/{id}", description="Find a Scrum board info by its id", response_model=schemas.Scrum)
async def read_item(id: int):
    db = get_db()    
    return scrum_service.ScrumService.get_scrum_by_id(db, id)    


@router.get("", description="Find a Scrum board info by its title", response_model=schemas.Scrum)
async def read_item(title: str):
    db = get_db()    
    return scrum_service.ScrumService.get_scrum_by_title(db, title)    


@router.post("/", description="Save new Scrum board", response_model=schemas.Scrum)
async def add_item(scrum: schemas.Scrum, db: Session = Depends(get_db)):
    db = get_db()
    sc = scrum_service.ScrumService.get_scrum_by_title(db, title=scrum.title)
    if sc:
        raise HTTPException(status_code=400, detail="Task já cadastrada")    
    close_db(db)
    db = get_db()
    sc = scrum_service.ScrumService.create_scrum(db, scrum=scrum)
    close_db(db)
    return sc

    


@router.put("/{id}", description="Update a Scrum board with specific id", response_model=schemas.Scrum)
async def update_item(id: int, scrum: schemas.Scrum):
    db = get_db()
    
    sc1 = scrum_service.ScrumService.update_scrum(db, id, scrum)
    return sc1


@router.delete("/{id}", description="Delete Scrum board with specific id")
async def delete_item(id: int):
    db = get_db()
    scrum_service.ScrumService.delete_scrum(db, id)
    return 'Ok'

@router.get("/{scrumId}/tasks/", description="View a list of all tasks for a Scrum with provided id", response_model=List[schemas.Task])
async def get_all_tasks_in_scrum(scrumId: int):
    db = get_db()    
    sc = scrum_service.ScrumService.get_scrum_by_id(db, scrumId)
    return sc.tasks

@router.post("/{scrumId}/tasks/", description="Save new Task and assign it to Scrum board", response_model=schemas.Scrum)
async def create_task_assigned_to_scrum(scrumId: int, taskDTO: schemas.TaskCreate, db: Session = Depends(get_db)):    
    db = get_db()
    sc = scrum_service.ScrumService.add_new_task_to_scrum(db, scrumId, taskDTO)
    close_db(db)
    return sc