from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Branch(Base):
  __tablename__ = "branches"

  branch_id = Column(String(20), primary_key=True)
  branch_name = Column(String(100), nullable=False)
  city = Column(String(100), index=True)
  state = Column(String(100))
  manager_name = Column(String(100))
  ifsc_code = Column(String(11))
  status = Column(String(20))

  accounts = relationship("Account", back_populates="branch")