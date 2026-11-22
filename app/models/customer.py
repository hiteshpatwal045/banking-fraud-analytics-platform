from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Customer(Base):
  __tablename__ = "customers"

  customer_id = Column(String(20), primary_key=True)
  customer_name = Column(String(100), nullable=False)
  email = Column(String(150), nullable=False)
  mobile = Column(String(10), nullable=False)
  city = Column(String(100), index=True)
  customer_type = Column(String(20), nullable=False, index=True)
  registration_date = Column(Date, nullable=False)
  status = Column(String(20), nullable=False)

  accounts = relationship("Account", back_populates="customer")
  loans = relationship("Loan", back_populates="customer")