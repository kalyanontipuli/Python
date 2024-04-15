from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from Models.models import GrammarSchools
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
    prefix='/grammer_schools',
    tags=['grammer_Schools']
)

class Grammar_School(BaseModel):
    grammer_school_name:str=Field(min_length=3)

def validate_grammar_school_id(grammar_school_id: int):
    if grammar_school_id < 1:
        raise HTTPException(status_code=404, detail="grammar school ID must be greater than 0")

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return  db.query(GrammarSchools).order_by(GrammarSchools.grammar_school_id).all()

@router.get("/school/{grammar_school_id}")
async def get_school_by_id(db:db_dependency,grammar_school_id:int):
    validate_grammar_school_id(grammar_school_id)
    school =  db.query(GrammarSchools).filter(GrammarSchools.grammar_school_id==grammar_school_id).first()
    if school is not None:
        return school
    else:
        raise HTTPException(status_code=404,detail='Subject Not found')
    
@router.post("/school",status_code=status.HTTP_201_CREATED)
async def create_grammar_school(db:db_dependency,school:Grammar_School):
    max_id = db.query(func.max(GrammarSchools.grammar_school_id)).scalar() or 0
    new_id=max_id+1
    school_model = GrammarSchools(grammar_school_id=new_id,grammar_school_name=school.grammar_school_name)
    db.add(school_model)
    db.commit()


@router.put("/school/{grammer_school_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_subject(db:db_dependency,grammar_school_id:int,school:Grammar_School):
    validate_grammar_school_id(grammar_school_id)
    school_model = db.query(GrammarSchools).filter(GrammarSchools.grammar_school_id==grammar_school_id).first()
    if school_model is None:
        raise HTTPException(status_code=404,detail="subject not found")
    
    school_model.grammar_school_name = school.grammer_school_name

    db.add(school_model)
    db.commit()

@router.delete("/delete_grammar_school/{grammar_school_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_grammar_school(db:db_dependency,grammar_school_id:int):
    validate_grammar_school_id(grammar_school_id)
    school = db.query(GrammarSchools).filter(GrammarSchools.grammar_school_id==grammar_school_id).first()
    if school is None:
        raise HTTPException(status_code=404,detail="Invalid school Id")
    
    db.delete(school)
    db.commit()
