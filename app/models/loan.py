from sqlalchemy import Column, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Loan(Base):
  __tablename__ = "loans"

  loan_id = Column(String(20), primary_key=True)
  customer_id = Column(String(20), ForeignKey("customers.customer_id"),nullable=False, index=True)
  loan_type = Column(String(30), nullable=False, index=True)
  loan_amount = Column(Numeric(15, 2), nullable=False)
  interest_rate = Column(Numeric(5, 2), nullable=False)
  loan_start_date = Column(Date, nullable=False)
  loan_status = Column(String(20), nullable=False)

  customer = relationship("Customer", back_populates="loans")