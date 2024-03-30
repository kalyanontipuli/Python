from fastapi import FastAPI
from database import engine
from routers import subjects,table_of_contents,private_schools,grammer_schools,exam_boards,publishers,papers
import models


app=FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(subjects.router)
app.include_router(table_of_contents.router)
app.include_router(private_schools.router)
app.include_router(grammer_schools.router)
app.include_router(exam_boards.router)
app.include_router(publishers.router)
app.include_router(papers.router)