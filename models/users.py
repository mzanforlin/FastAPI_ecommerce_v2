from sqlalchemy import Column, Integer, String, DateTime, func
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key= True)
    name = Column(String(100), nullable= False)
    password = Column(String(100), nullable= False)
    email = Column(String(100), nullable=False, unique= True)
    create_date = Column(DateTime,server_default= func.now())