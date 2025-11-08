from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    company = Column(String(100))
    phone = Column(String(20))
    email = Column(String(255))
    address = Column(Text)
    client_type = Column(String(20), default="potential")  # potential or active
    notes = Column(Text)
    employee_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relaciones
    employee = relationship("User")