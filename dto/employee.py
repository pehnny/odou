from typing import Optional
from pydantic import BaseModel

class CreateEmployeeDTO(BaseModel):
    firstname: str
    lastname: str

class EmployeeDTO(BaseModel):
    id: int
    firstname: str
    lastname: str
    team_id: Optional[int]
    role_id: Optional[int]