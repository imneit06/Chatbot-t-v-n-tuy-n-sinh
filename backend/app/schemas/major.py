from pydantic import BaseModel
from typing import Optional

class MajorBase(BaseModel):
    code: str
    name: str
    fee: str
    admission_blocks: str
    description: Optional[str] = None

class MajorCreate(MajorBase):
    pass

class MajorResponse(MajorBase):
    id: int

    class Config:
        from_attributes = True # Dành cho Pydantic V2