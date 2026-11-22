from sqlalchemy import Column, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Account(Base):
  __tablename__ = "accounts"

  account_id = Column(String(20), primary_key=True)
  customer_id = Column(String(20), ForeignKey("customers.customer_id"))
  account_type = Column(String(20))
  branch_id = Column(String(20), ForeignKey("branches.branch_id"))
  balance = Column(Numeric(15, 2))
  opening_date = Column(Date)
  account_status = Column(String(20))

  customer = relationship("Customer", back_populates="accounts")
  branch = relationship("Branch", back_populates="accounts")
  transactions = relationship("Transaction", back_populates="account")