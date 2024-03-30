from sqlalchemy import Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Subjects(Base):
    __tablename__ = 'subjects'
    
    subject_id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)


class TableOfContents(Base):
    __tablename__ = 'table_of_contents'

    subject_id = Column(Integer, ForeignKey('subjects.subject_id'), primary_key=True)
    toc_id = Column(Integer, primary_key=True)
  
    title = Column(String)
    link_to_page = Column(String)

    subject = relationship("Subjects")

    # Define a composite primary key constraint explicitly
    __table_args__ = (
        PrimaryKeyConstraint('toc_id', 'subject_id'),
    )

class Publishers(Base):
    __tablename__ = 'publishers'
    
    publisher_id = Column(Integer, primary_key=True,autoincrement=True)
    publisher_name = Column(String)

class ExamBoards(Base):
    __tablename__ = 'exam_boards'
    
    exam_board_id = Column(Integer, primary_key=True,autoincrement=True)
    exam_board_name = Column(String)

class PrivateSchools(Base):
    __tablename__ = 'private_schools'
    
    private_school_id = Column(Integer, primary_key=True,autoincrement=True)
    private_school_name = Column(String)

class GrammarSchools(Base):
    __tablename__ = 'grammar_schools'
    
    grammar_school_id = Column(Integer, primary_key=True,autoincrement=True)
    grammar_school_name = Column(String)


class Papers(Base):
    __tablename__ = 'papers'
    
    paper_id = Column(Integer, primary_key=True, autoincrement=True)
    paper_name = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    toc_id = Column(Integer)
    private_school_id = Column(Integer, ForeignKey('private_schools.private_school_id'))
    grammar_school_id = Column(Integer, ForeignKey('grammar_schools.grammar_school_id'))
    exam_board_id = Column(Integer, ForeignKey('exam_boards.exam_board_id'))
    publisher_id = Column(Integer, ForeignKey('publishers.publisher_id'))
    year = Column(Integer)
    link_to_paper = Column(String)
   
    toc = relationship("TableOfContents")
    private_school = relationship("PrivateSchools")
    grammar_school = relationship("GrammarSchools")
    publisher = relationship("Publishers")
    exam_board = relationship("ExamBoards")

    # Define the composite foreign key constraint
    __table_args__ = (
        ForeignKeyConstraint(
            ['toc_id', 'subject_id'],
            ['table_of_contents.toc_id', 'table_of_contents.subject_id']
        ),
    )






