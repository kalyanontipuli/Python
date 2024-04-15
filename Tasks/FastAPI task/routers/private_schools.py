from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel,Field, HttpUrl
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from Models.models import PrivateSchools
from Database.database import SessionLocal

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]
router = APIRouter(
    prefix='/private_schools',
    tags=['private_Schools']
)


class Private_School(BaseModel):
    private_school_name:str=Field(min_length=3)

def validate_private_school_id(private_school_id: int):
    if private_school_id < 1:
        raise HTTPException(status_code=404, detail="Private school ID must be greater than 0")

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return  db.query(PrivateSchools).order_by(PrivateSchools.private_school_id).all()

@router.get("/school/{private_school_id}")
async def get_school_by_id(db:db_dependency,private_school_id:int):
    max_id = db.query(func.max(PrivateSchools.private_school_id)).scalar() or 0
    if private_school_id<0:
        raise HTTPException(status_code=404,detail="private school id must be greater than 0 and less than {}".format(max_id))
    school =  db.query(PrivateSchools).filter(PrivateSchools.private_school_id==private_school_id).first()
    if school is not None:
        return school
    else:
        raise HTTPException(status_code=404,detail='Subject Not found')
    
@router.post("/school", status_code=status.HTTP_201_CREATED)
async def create_school(db: db_dependency, school: Private_School):
    max_id = db.query(func.max(PrivateSchools.private_school_id)).scalar() or 0
    new_id = max_id + 1
    school_model = PrivateSchools(private_school_id=new_id, private_school_name=school.private_school_name)
    db.add(school_model)
    db.commit()
    db.refresh(school_model)
    return school_model

@router.put("/school/{private_school_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_subject(db:db_dependency,private_school_id:int,school:Private_School):
    validate_private_school_id(private_school_id)
    school_model = db.query(PrivateSchools).filter(PrivateSchools.private_school_id==private_school_id).first()
    if school_model is None:
        raise HTTPException(status_code=404,detail="school not found")
    
    school_model.private_school_name = school.private_school_name

    db.add(school_model)
    db.commit()

@router.delete("/delete_private_school/{private_school_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_private_school(db:db_dependency,private_school_id:int):
    validate_private_school_id(private_school_id)
    school = db.query(PrivateSchools).filter(PrivateSchools.private_school_id==private_school_id).first()
    if school is None:
        raise HTTPException(status_code=404,detail="Invalid school Id")
    
    db.delete(school)
    db.commit()
