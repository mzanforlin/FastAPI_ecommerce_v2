from sqlalchemy import Column, Integer, String, DateTime, func
from .base import Base

class User(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key= True)
    product = Column(String(100), nullable= False)
    category = Column(String(100), nullable= False)
    price = Column(Integer, nullable=False)
    create_date = Column(DateTime,server_default= func.now())