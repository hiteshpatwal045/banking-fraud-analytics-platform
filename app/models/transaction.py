from sqlalchemy import Column, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Transaction(Base):
  __tablename__ = "transactions"

  transaction_id = Column(String(20), primary_key=True)
  account_id = Column(String(20), ForeignKey("accounts.account_id"))
  transaction_type = Column(String(10))
  transaction_amount = Column(Numeric(15, 2))
  transaction_date = Column(Date, index=True)
  transaction_mode = Column(String(20))
  merchant_category = Column(String(50))
  transaction_category = Column(String(20))
  risk_status = Column(String(20))

  account = relationship("Account", back_populates="transactions")