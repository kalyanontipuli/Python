from typing import Annotated
from fastapi import  APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from sqlalchemy import func
from starlette import status
from sqlalchemy.orm import Session
from models import Papers
from database import SessionLocal
from routers.private_schools import Private_School

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

class Paper(BaseModel):
    __tablename__ = 'papers'
    
    paper_name:str
    subject_id :int
    toc_id :int
    year :int
    link_to_paper :str

class PaperName(BaseModel):
    paper_name: str

class PaperLink(BaseModel):
    link_to_paper: str
class PaperYear(BaseModel):
    year: int

router = APIRouter(
    prefix='/papers',
    tags=['papers']
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    papers=   db.query(Papers).order_by(Papers.paper_id).all()
    
    filtered_papers = []
    for paper in papers:
        filtered_paper = {}
        
        for key, value in paper.__dict__.items():
            if value is not None:
                filtered_paper[key] = value
        filtered_papers.append(filtered_paper)
    return filtered_papers


@router.get("/paper/{paper_id}")
async def get_school_by_id(db:db_dependency,paper_id:int):
    paper =  db.query(Papers).filter(Papers.paper_id==paper_id).first()
    if paper is not None:
        return paper
    else:
        raise HTTPException(status_code=404,detail='Subject Not found')

@router.get("/english/{table_of_contents_id}")
async def get_english_papers(db:db_dependency,table_of_contents_id:int):
   

    result = []
    if table_of_contents_id==1:

        private_english_papers =  db.query( Papers.private_school_id,Papers.paper_name, Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==1).order_by(Papers.paper_name).all()
        for paper in private_english_papers:
            result.append({"private_school_id":paper.private_school_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    

    elif table_of_contents_id==2:
        grammer_english_papers =  db.query(Papers.grammar_school_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==1).order_by(Papers.paper_name).all()
        for paper in grammer_english_papers:
            result.append({"grammer_school_id":paper.grammar_school_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    elif table_of_contents_id==3:
            exam_board__english_papers =  db.query(Papers.exam_board_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==1).order_by(Papers.paper_name).all()
            for paper in exam_board__english_papers:
                result.append({"exam_board_id":paper.exam_board_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
            return result
    elif table_of_contents_id==4:
        publish_english_papers =  db.query(Papers.publisher_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==1).order_by(Papers.paper_name).all()
        for paper in publish_english_papers:
            result.append({"publisher_id":paper.publisher_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    else:
        raise HTTPException(status_code=404,detail="table_of_content_id should between 1 and 4")
    
@router.get("/maths/{table_of_contents_id}")
async def get_maths_papers(db:db_dependency,table_of_contents_id:int):
    
    result = []
    if table_of_contents_id==1:
        private_maths_papers =  db.query( Papers.private_school_id,Papers.paper_name, Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==2).order_by(Papers.paper_name).all()
        for paper in private_maths_papers:
            result.append({"private_school_id":paper.private_school_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    elif table_of_contents_id==2:
        grammer_maths_papers =  db.query(Papers.grammar_school_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==2).order_by(Papers.paper_name).all()
        for paper in grammer_maths_papers:
            result.append({"grammer_school_id":paper.grammar_school_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    elif table_of_contents_id==3:
            exam_board_maths_papers =  db.query(Papers.exam_board_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==2).order_by(Papers.paper_name).all()
            for paper in exam_board_maths_papers:
                result.append({"exam_board_id":paper.exam_board_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
            return result
    elif table_of_contents_id==4:
        publish_maths_papers =  db.query(Papers.publisher_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==2).order_by(Papers.paper_name).all()
        for paper in publish_maths_papers:
            result.append({"publisher_id":paper.publisher_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    else:
        raise HTTPException(status_code=404,detail="table_of_content_id should between 1 and 4")


    
@router.get("/verbal-Reasoning/{table_of_contents_id}")
async def get_verbal_Reasoning_papers(db:db_dependency,table_of_contents_id:int):
    
    result = []
    if table_of_contents_id==1:
        private_verbal_papers =  db.query( Papers.private_school_id,Papers.paper_name, Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==3).order_by(Papers.paper_name).all()
        for paper in private_verbal_papers:
            result.append({"private_verbal_id":paper.private_school_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    elif table_of_contents_id==2:
        grammer_verbal_papers =  db.query(Papers.grammar_school_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==3).order_by(Papers.paper_name).all()
        for paper in grammer_verbal_papers:
            result.append({"grammer_verbal_id":paper.grammar_school_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    elif table_of_contents_id==3:
            exam_board_verbal_papers =  db.query(Papers.exam_board_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==3).order_by(Papers.paper_name).all()
            for paper in exam_board_verbal_papers:
                result.append({"exam_board_id":paper.exam_board_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
            return result
    elif table_of_contents_id==4:
        publish_verbal_papers =  db.query(Papers.publisher_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==3).order_by(Papers.paper_name).all()
        for paper in publish_verbal_papers:
            result.append({"publisher_id":paper.publisher_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    else:
        raise HTTPException(status_code=404,detail="table_of_content_id should between 1 and 4")

    
@router.get("/non-verbal-Reasoning/{table_of_contents_id}")
async def get_non_verbal_Reasoning_papers(db:db_dependency,table_of_contents_id:int):
    result = []
    if table_of_contents_id==1:
            papers =  db.query(Papers.exam_board_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==4).order_by(Papers.paper_name).all()
            for paper in papers:
                result.append({"exam_board_id":paper.exam_board_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
            return result
    elif table_of_contents_id==2:
        papers =  db.query(Papers.publisher_id,Papers.paper_name,Papers.link_to_paper).filter(Papers.toc_id==table_of_contents_id,Papers.subject_id==4).order_by(Papers.paper_name).all()
        for paper in papers:
            result.append({"publisher_id":paper.publisher_id,"paper_name":paper.paper_name,"paper_link":paper.link_to_paper})
        return result
    else:
        raise HTTPException(status_code=404,detail="table_of_content_id should between 1 and 2")



# @router.post("/paper",status_code=status.HTTP_201_CREATED)
# async def create_paper(db:db_dependency,paper:Paper):

#     paper_model=""
#     max_id = db.query(func.max(Papers.paper_id)).scalar() or 0
#     new_id = max_id + 1

#     if paper.private_school_id:
#          if paper.grammar_school_id or paper.exam_board_id or paper.publisher_id:
#              raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
#          else:
#              paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,
#                                 subject_id=paper.subject_id,toc_id=paper.toc_id,
#                                 private_school_id=paper.private_school_id,year=paper.year,
#                                 link_to_paper=paper.link_to_paper)
    

#     elif paper.grammar_school_id:
#          if paper.private_school_id or paper.exam_board_id or paper.publisher_id:
#              raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
#          else:
#              paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,
#                                 subject_id=paper.subject_id,toc_id=paper.toc_id,
#                                 grammar_school_id=paper.grammar_school_id,year=paper.year,
#                                 link_to_paper=paper.link_to_paper)

#     elif paper.exam_board_id:
#         if paper.private_school_id or paper.grammar_school_id or paper.publisher_id:
#             raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
#         else:
#             paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,subject_id=paper.subject_id,
#                                toc_id=paper.toc_id,exam_board_id=paper.exam_board_id,year=paper.year,
#                                link_to_paper=paper.link_to_paper)
    
#     elif paper.publisher_id:
#         if paper.private_school_id or paper.exam_board_id or paper.grammar_school_id:
#             raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
#         else:
#             paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,subject_id=paper.subject_id,
#                                toc_id=paper.toc_id,publisher_id=paper.publisher_id,year=paper.year,
#                                link_to_paper=paper.link_to_paper)
    
#     if paper_model is None:
#         raise HTTPException(status_code=400,detail="ensure to give values to paper cateogry")
#     else:
#         db.add(paper_model)
#         db.commit()



@router.post("/paper/{category_type}/{category_value}",status_code=status.HTTP_201_CREATED)
async def create_paper(db:db_dependency,paper:Paper,category_type:int,category_value:int):

    paper_model=""
    max_id = db.query(func.max(Papers.paper_id)).scalar() or 0
    new_id = max_id + 1

    if category_type is not None and category_value is not None:
        if category_type==1:
            paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,
                                subject_id=paper.subject_id,toc_id=paper.toc_id,
                                private_school_id=category_value,year=paper.year,
                                link_to_paper=paper.link_to_paper)
        

        elif category_type==2:
            paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,
                                subject_id=paper.subject_id,toc_id=paper.toc_id,
                                grammar_school_id=category_value,year=paper.year,
                                link_to_paper=paper.link_to_paper)

        elif category_type==3:
            paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,subject_id=paper.subject_id,
                                toc_id=paper.toc_id,exam_board_id=category_value,year=paper.year,
                                link_to_paper=paper.link_to_paper)
        
        elif category_type==4:
                paper_model=Papers(paper_id=new_id,paper_name=paper.paper_name,subject_id=paper.subject_id,
                                toc_id=paper.toc_id,publisher_id=category_value,year=paper.year,
                                link_to_paper=paper.link_to_paper)
        else:
            raise HTTPException(status_code=404,detail="select proper category type between 1 and 4 and give proper category value")
    else:
        raise HTTPException(status_code=404,detail="provide values for category type and category value :")
    
    db.add(paper_model)
    db.commit()



@router.put("/update_paper_name/{paper_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_paper_name(db:db_dependency,paper_id:int,paper_name:PaperName):
    
    paper_model=db.query(Papers).filter(Papers.paper_id==paper_id).first()

    if paper_model is None:
        raise HTTPException(status_code=400,detail="paper not found")
    paper_model.paper_name  = paper_name

    db.add(paper_model)
    db.commit()

@router.put("/update_paper_link/{paper_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_paper_link(db:db_dependency,paper_id:int,link_to_paper:PaperLink):
    
    paper_model=db.query(Papers).filter(Papers.paper_id==paper_id).first()

    if paper_model is None:
        raise HTTPException(status_code=400,detail="paper not found")
    
    paper_model.link_to_paper  = link_to_paper

    db.add(paper_model)
    db.commit()

@router.put("/update_paper_year/{paper_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_paper_year(db:db_dependency,paper_id:int,year:PaperYear):
    
    paper_model=db.query(Papers).filter(Papers.paper_id==paper_id).first()

    if paper_model is None:
        raise HTTPException(status_code=400,detail="paper not found")
    
    paper_model.year = year

    db.add(paper_model)
    db.commit()

@router.put("/update_paper/{paper_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_paper(db:db_dependency,paper_id:int,paper:Paper):
    
    paper_model=db.query(Papers).filter(Papers.paper_id==paper_id).first()

    if paper_model is None:
        raise HTTPException(status_code=400,detail="paper not found")
    
    paper_model.paper_name  = paper.paper_name
    paper_model.subject_id = paper.subject_id
    paper_model.toc_id = paper.toc_id
    paper_model.year = paper.year
    paper_model.link_to_paper =  paper.link_to_paper
    # if paper_model.private_school_id:
    #      if paper.grammar_school_id or paper.exam_board_id or paper.publisher_id:
    #          raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
    #      else:
    #             paper_model.private_school_id = paper.private_school_id

    # elif paper.grammar_school_id:
    #      if paper.private_school_id or paper.exam_board_id or paper.publisher_id:
    #          raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
    #      else:
    #          paper_model.grammer_school_id = paper.grammar_school_id
    
    # elif paper.exam_board_id:
    #     if paper.private_school_id or paper.grammar_school_id or paper.publisher_id:
    #         raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
    #     else:
    #         paper_model.exam_board_id = paper.exam_board_id
    # elif paper.publisher_id:
    #     if paper.private_school_id or paper.exam_board_id or paper.grammar_school_id:
    #         raise HTTPException(status_code=400, detail="Invalid input for a paper belonging to only one cateogry.")
    #     else:
    #         paper_model.publisher_id = paper.publisher_id

    db.add(paper_model)
    db.commit()

@router.delete("/delete-paper/{paper_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_paper(db:db_dependency,paper_id:int):

    paper = db.query(Papers).filter(Papers.paper_id==paper_id).first()
    if paper is None:
        raise HTTPException(status_code=404,detail="Invalid paper id")
    
    db.delete(paper)
    db.commit()
    



