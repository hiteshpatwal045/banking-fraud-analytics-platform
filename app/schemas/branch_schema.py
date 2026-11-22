from pydantic import BaseModel, ConfigDict

class BranchSchema(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  branch_id: str
  branch_name: str
  city: str | None = None
  state: str | None = None
  manager_name: str | None = None
  ifsc_code: str | None = None
  status: str | None = None