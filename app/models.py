from sqlalchemy import Column , String, Integer
from app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

class User(Base):
    __tablename__ ="users"

    id=Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    hashed_pass = Column(String)