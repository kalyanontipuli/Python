from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from models import ExamBoards
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
    prefix='/Exam_boards',
    tags=['Exam_boards']
)

class Exam_Board(BaseModel):
    exam_board_name : str


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return  db.query(ExamBoards).order_by(ExamBoards.exam_board_id).all()

@router.get("/examboard/{exam_board_id}")
async def get_school_by_id(db:db_dependency,exam_board_id:int):
    exam_board =  db.query(ExamBoards).filter(ExamBoards.exam_board_id==exam_board_id).first()
    if exam_board is not None:
        return exam_board
    else:
        raise HTTPException(status_code=404,detail='exam board not found')
    
    
@router.post("/examboard",status_code=status.HTTP_201_CREATED)
async def create_exam_board(db:db_dependency,exam_board:Exam_Board):
    max_id = db.query(func.max(ExamBoards.exam_board_id)).scalar() or 0
    new_id=max_id+1
    board_model = ExamBoards(exam_board_id=new_id,exam_board_name=exam_board.exam_board_name)
    db.add(board_model)
    db.commit()

@router.put("/examboard/{exam_board_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_exam_board(db:db_dependency,exam_board_id:int,exam_board:Exam_Board):

    exam_board_model = db.query(ExamBoards).filter(ExamBoards.exam_board_id==exam_board_id).first()
    if exam_board_model is None:
        raise HTTPException(status_code=404,detail="subject not found")
    
    exam_board_model.exam_board_name=exam_board.exam_board_name
    db.add(exam_board_model)
    db.commit()

@router.delete("/delete_exam_board/{exam_board_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_exam_board(db:db_dependency,exam_board_id:int):

    exam_board = db.query(ExamBoards).filter(ExamBoards.exam_board_id==exam_board_id).first()
    if exam_board is None:
        raise HTTPException(status_code=404,detail="Invalid exam board id")
    
    db.delete(exam_board)
    db.commit()