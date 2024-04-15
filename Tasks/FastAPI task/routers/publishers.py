from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from Models.models import Publishers
from Database.database import SessionLocal

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

router = APIRouter(
    prefix='/publishers',
    tags=['publishers']
)

class Publisher(BaseModel):
    publisher_name:str=Field(min_length=3)


def validate_publisher_id(publisher_id: int):
    if publisher_id < 1:
        raise HTTPException(status_code=404, detail="publisher ID must be greater than 0")
    
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return  db.query(Publishers).order_by(Publishers.publisher_id).all()

@router.get("/publisher/{publisher_id}")
async def get_school_by_id(db:db_dependency,publisher_id:int):
    validate_publisher_id(publisher_id)
    publisher =  db.query(Publishers).filter(Publishers.publisher_id==publisher_id).first()
    if publisher is not None:
        return publisher
    else:
        raise HTTPException(status_code=404,detail='Subject Not found')


@router.post("/publisher",status_code=status.HTTP_201_CREATED)
async def create_publisher(db:db_dependency,publisher:Publisher):
    max_id = db.query(func.max(Publishers.publisher_id)).scalar() or 0
    new_id=max_id+1
    publisher_model = Publishers(publisher_id=new_id,publisher_name=publisher.publisher_name)
    db.add(publisher_model)
    db.commit()

@router.put("/{publisher_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_publisher(db:db_dependency,publisher_id:int,publisher:Publisher):
    validate_publisher_id(publisher_id)
    publisher_model = db.query(Publishers).filter(Publishers.publisher_id==publisher_id).first()
    if publisher_model is None:
        raise HTTPException(status_code=404,detail="subject not found")
    
    publisher_model.publisher_name=publisher.publisher_name
    db.add(publisher_model)
    db.commit()

@router.delete("/delete_publisher/{publisher_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_publisher(db:db_dependency,publisher_id:int):
    validate_publisher_id(publisher_id)
    publisher = db.query(Publishers).filter(Publishers.publisher_id==publisher_id).first()
    if publisher is None:
        raise HTTPException(status_code=404,detail="Invalid publisher id")
    
    db.delete(publisher)
    db.commit()
