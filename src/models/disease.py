"""
Author:- Jagannath Hari
File Name:- disease.py
Date:- 11/9/2023
Time:- 3:34
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String , 

Base = declarative_base()


class Disease(Base):
    __tablename__ = "disease"
    name = Column(String)
    age = Column(Integer)
    contact = Column(String)
    email  = Column(String)

