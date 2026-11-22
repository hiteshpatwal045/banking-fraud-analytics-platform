from datetime import date
from pydantic import BaseModel, ConfigDict

class TransactionCreate(BaseModel):
  transaction_id: str
  account_id: str
  transaction_type: str
  transaction_amount: float
  transaction_date: date
  transaction_mode: str
  merchant_category: str | None = None


class TransactionResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  transaction_id: str
  account_id: str
  transaction_type: str
  transaction_amount: float
  transaction_date: date
  transaction_mode: str
  merchant_category: str | None = None
  transaction_category: str | None = None
  risk_status: str | None = None