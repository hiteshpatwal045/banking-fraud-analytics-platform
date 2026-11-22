from datetime import date
from pydantic import BaseModel, ConfigDict

class CustomerCreate(BaseModel):
  customer_id: str
  customer_name: str
  email: str
  mobile: str
  city: str | None = None
  customer_type: str
  registration_date: date
  status: str

class CustomerUpdate(BaseModel):
  customer_name: str | None = None
  email: str | None = None
  mobile: str | None = None
  city: str | None = None
  customer_type: str | None = None
  status: str | None = None

class CustomerResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  customer_id: str
  customer_name: str
  email: str
  mobile: str
  city: str | None = None
  customer_type: str
  registration_date: date
  status: str