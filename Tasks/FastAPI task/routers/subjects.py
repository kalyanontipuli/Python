from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException,Path
from pydantic import BaseModel,Field
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from Models.models import Subjects
from Database.database import SessionLocal

import logging
logging.basicConfig(level=logging.INFO, filename="app.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

router = APIRouter(
    prefix='/subjects',
    tags=['subjects']
)

class Subject(BaseModel):
    name:str = Field(min_length=3)



@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    logging.info("Read all endpoint accessed")
    return  db.query(Subjects).order_by(Subjects.subject_id).all()

@router.get("/subject/{subject_id}")
async def get_subject_by_id(db:db_dependency,subject_id:int=Path(gt=0)):
    logging.info("subject with id {} accessed".format(subject_id))
    subject =  db.query(Subjects).filter(Subjects.subject_id==subject_id).first()
    max_id = db.query(func.max(Subjects.subject_id)).scalar() or 0
    if subject is not None:
        logging.info("subject returned")
        return subject
    else:
        logging.warning("user entered a wroung id")
        raise HTTPException(status_code=404,detail="Id should between {} and {}".format(0,max_id+1))

@router.post("/subject",status_code=status.HTTP_201_CREATED)
async def add_subject(db:db_dependency,subject:Subject):
    max_id = db.query(func.max(Subjects.subject_id)).scalar() or 0
    new_id = max_id + 1
    subject_model = Subjects(subject_id=new_id,name=subject.name)
    db.add(subject_model)
    db.commit()
    
@router.put("/subject/{subject_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_subject(db:db_dependency,subject_id:int,subject:Subject):

    subject_model = db.query(Subjects).filter(Subjects.subject_id==subject_id).first()
    if subject_model is None:
        raise HTTPException(status_code=404,detail="subject not found")
    
    subject_model.name = subject.name

    db.add(subject_model)
    db.commit()
    
@router.delete("/delete_subject/{subject_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(db:db_dependency,subject_id:int):
    max_id = db.query(func.max(Subjects.subject_id)).scalar() or 0
    if subject_id<1:
        raise HTTPException(status_code=404,detail='Subject id must be greater than 0')
    elif subject_id>max_id:
        raise HTTPException(status_code=404,detail='Id should between {} and {}'.format(0,max_id+1))
    subject = db.query(Subjects).filter(Subjects.subject_id==subject_id).first()
    if subject is None:
        raise HTTPException(status_code=404,detail="Invalid subject Id")
    
    db.delete(subject)
    db.commit()
