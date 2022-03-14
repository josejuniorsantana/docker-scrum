from sqlalchemy.orm import Session

from infrastructure import schemas, models
from sqlalchemy import select, update, delete, values


class TaskService():
    def get_all(db: Session):
        return next(db).query(models.Task).all()

    def get_task_by_id(db: Session, id: int):
        return next(db).query(models.Task).filter(models.Task.id == id).first()


    def get_task_by_title(db: Session, title: str):
        return next(db).query(models.Task).filter(models.Task.title == title).first()


    def get_tasks(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Task).offset(skip).limit(limit).all()


    def create_task(db: Session, task: schemas.TaskCreate):
        db_task = models.Task(title=task.title, scrum_id = task.scrum_id)
        db_task.color = task.color
        db_task.status = task.status
        db_task.description = task.description + '\n - API Python'

        db1 = next(db)
        db1.add(db_task)
        db1.commit()
        db1.refresh(db_task)
        return db_task

    def update_task(db: Session, id: int, task: schemas.TaskCreate):
        db1 = next(db)        
        sc = db1.query(models.Task).filter(models.Task.id == id).first()
        sc.title = task.title
        sc.color = task.color
        sc.description = task.description + '\n - API Python'
        sc.status = task.status
        db1.merge(sc)
        db1.commit()
        db1.refresh(sc)
        return sc
        

    def delete_task(db: Session, id: int):        
        db1 = next(db)
        effected_rows = db1.query(models.Task).filter(models.Task.id == id).delete()
        
        if effected_rows == 0:
            return False
        else:
            db1.commit()
            return True

