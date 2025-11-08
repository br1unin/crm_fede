from sqlalchemy import Column, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    tractor_id = Column(Integer, ForeignKey("tractors.id"))
    employee_id = Column(Integer, ForeignKey("users.id"))
    sale_price = Column(Float, nullable=False)
    sale_date = Column(DateTime(timezone=True), server_default=func.now())
    notes = Column(Text)
    
    # Relaciones
    client = relationship("Client")
    tractor = relationship("Tractor")
    employee = relationship("User")