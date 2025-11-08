from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base

class Tractor(Base):
    __tablename__ = "tractors"
    
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(100), nullable=False)
    brand = Column(String(50), nullable=False)
    year = Column(Integer)
    price = Column(Float)
    status = Column(String(20), default="available")  # available, sold
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())