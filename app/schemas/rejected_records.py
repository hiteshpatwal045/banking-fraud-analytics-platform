from datetime import datetime
from pydantic import BaseModel, ConfigDict

class RejectedRecordSchema(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  source_file: str | None = None
  record_data: str | None = None
  rejection_reason: str | None = None
  rejected_at: datetime | None = None
  pipeline_run_id: str | None = None