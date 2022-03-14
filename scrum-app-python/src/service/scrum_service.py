from sqlalchemy.orm import Session

from infrastructure import schemas, models


class ScrumService():
    def get_all(db: Session):
        return next(db).query(models.Scrum).all()

    def get_scrum_by_id(db: Session, id: int):
        return next(db).query(models.Scrum).filter(models.Scrum.id == id).first()


    def get_scrum_by_title(db: Session, title: str):
        return next(db).query(models.Scrum).filter(models.Scrum.title == title).first()


    def get_scrums(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Scrum).offset(skip).limit(limit).all()


    def create_scrum(db: Session, scrum: schemas.ScrumCreate):
        db_scrum = models.Scrum(title="p-" + scrum.title)
        db1 = next(db)
        db1.add(db_scrum)
        db1.commit()
        db1.refresh(db_scrum)
        return db_scrum

    def update_scrum(db: Session, id: int, scrum: schemas.ScrumCreate):
        db1 = next(db)        
        sc = db1.query(models.Scrum).filter(models.Scrum.id == id).first()

        if "j-" in scrum.title[0:2]:
            scrum.title[0:2].replace('j','p')
        elif not "p-" in scrum.title[0:2]:
            scrum.title = "p-" + scrum.title

        sc.title = scrum.title
        db1.merge(sc)
        db1.commit()
        db1.refresh(sc)
        return sc
        

    def delete_scrum(db: Session, id: int):
        db1 = next(db)        
        db1.query(models.Scrum).filter(models.Scrum.id == id).delete()
        db1.commit()
        

    def add_new_task_to_scrum(db: Session, id: int, task: schemas.Task):
        db1 = next(db)
        #sc = db1.query(models.Scrum).filter(models.Scrum.id == id).first()
        db_task = models.Task(title=task.title, scrum_id = id)
        db_task.color = task.color
        db_task.status = task.status
        db_task.description = task.description + '\n - API Python'
        
        db1.add(db_task)
        db1.commit()
        db1.refresh(db_task)
        return db_task
    