from datetime import date
from pydantic import BaseModel, ConfigDict

class AccountCreate(BaseModel):
  account_id: str
  customer_id: str
  account_type: str
  branch_id: str
  balance: float
  opening_date: date
  account_status: str

class AccountUpdate(BaseModel):
  account_type: str | None = None
  branch_id: str | None = None
  balance: float | None = None
  account_status: str | None = None

class AccountResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  account_id: str
  customer_id: str
  account_type: str
  branch_id: str
  balance: float
  opening_date: date
  account_status: str