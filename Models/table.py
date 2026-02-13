from sqlalchemy import Column, Integer, String,Text,DateTime,ForeignKey
from datetime import datetime
from Database.database import Base

class Users(Base):
    __tablename__="Users"

    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(50), unique=True, index=True)
    hashed_Password=Column(String(255))
    role = Column(String, default="user")


class Task(Base):
    __tablename__="Task"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    owner_id=Column(Integer,ForeignKey("Users.id"), index=True)
    description = Column(String, nullable=True)
