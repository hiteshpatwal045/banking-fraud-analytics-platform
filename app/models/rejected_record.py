from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database.connection import Base

class RejectedRecord(Base):
  __tablename__ = "rejected_records"

  id = Column(Integer, primary_key=True, autoincrement=True)
  source_file = Column(String(50))
  record_data = Column(Text)
  rejection_reason = Column(String(255))
  rejected_at = Column(DateTime)
  pipeline_run_id = Column(String(50))