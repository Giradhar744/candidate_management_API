from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

class StatusEnum(str, Enum):
    applied = "applied"
    interview = "interview"
    selected = "selected"
    rejected = "rejected"

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    skill: str
    status: StatusEnum = StatusEnum.applied

class StatusUpdate(BaseModel):
    status: StatusEnum

class CandidateResponse(BaseModel):
    id: int
    name: str
    email: str
    skill: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}