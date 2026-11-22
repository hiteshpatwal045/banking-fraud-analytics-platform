from datetime import date
from pydantic import BaseModel, ConfigDict

class LoanSchema(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  loan_id: str
  customer_id: str
  loan_type: str
  loan_amount: float
  interest_rate: float
  loan_start_date: date
  loan_status: str