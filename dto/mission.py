from typing import Optional
from pydantic import BaseModel

class CreateMissionDTO(BaseModel):
    name: str
    client_id: Optional[int] = None

class MissionDTO(BaseModel):
    id: int
    name: str
    client_id: Optional[int]
