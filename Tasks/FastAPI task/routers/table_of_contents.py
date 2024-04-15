from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException,Path
from pydantic import BaseModel,Field
from starlette import status
from sqlalchemy.orm import Session
from Models.models import TableOfContents
from Database.database import SessionLocal

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]


class Table_Of_Contents(BaseModel):
    subject_id:int=Field(gt=0,description="subject  id should be greater than 0")
    toc_id:int=Field(gt=0,description="toc_id should be greater than 0")
    title:str=Field(min_length=3)
    link_to_page:str=Field(min_length=5)


router = APIRouter(
    prefix='/table_of_contents',
    tags=['table_of_contents']
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    l = db.query(TableOfContents).all()
    if l is not None:
        return l
    else:
        raise HTTPException(status_code=404,detail="No Items found")

@router.get("/contents/{subject_id}")
async def get_contents_by_subject_id(db:db_dependency,subject_id:int=Path(gt=0)):
    contents =  db.query(TableOfContents).filter(TableOfContents.subject_id==subject_id).all()
    if contents is not None:
        return contents
    else:
        raise HTTPException(status_code=404,detail='Subject Not found')
    
@router.post("/contents",status_code=status.HTTP_201_CREATED)
async def create_table_of_contents(db:db_dependency,toc:Table_Of_Contents):
    toc_model  = TableOfContents(subject_id=toc.subject_id,toc_id=toc.toc_id,title=toc.title,link_to_page=toc.link_to_page)
    db.add(toc_model)
    db.commit()

@router.put("/contents/{subject_id}/{toc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_table_of_contents(db:db_dependency,subject_id:int,toc_id:int,toc:Table_Of_Contents):
    toc_model = db.query(TableOfContents).filter(TableOfContents.subject_id==subject_id,TableOfContents.toc_id==toc_id).first()
    if toc_model is None:
        raise HTTPException(status_code=404,detail="table of content model not found")
    
    toc_model.title = toc.title
    toc_model.link_to_page = toc.link_to_page

    db.add(toc_model)
    db.commit()

@router.delete("/delete_toc/{subject_id}/{toc_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(db:db_dependency,subject_id:int,toc_id:int):

    toc = db.query(TableOfContents).filter(TableOfContents.subject_id==subject_id,TableOfContents.toc_id==toc_id).first()
    if toc is None:
        raise HTTPException(status_code=404,detail="Invalid subject_id or toc_id")
    
    db.delete(toc)
    db.commit()

