from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from models import Subjects
from database import SessionLocal

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
    name:str



@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return  db.query(Subjects).order_by(Subjects.subject_id).all()

@router.get("/subject/{subject_id}")
async def get_subject_by_id(db:db_dependency,subject_id:int):
    subject =  db.query(Subjects).filter(Subjects.subject_id==subject_id).first()
    if subject is not None:
        return subject
    else:
        raise HTTPException(status_code=404,detail='Subject Not found')

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

    subject = db.query(Subjects).filter(Subjects.subject_id==subject_id).first()
    if subject is None:
        raise HTTPException(status_code=404,detail="Invalid subject Id")
    
    db.delete(subject)
    db.commit()



    



    