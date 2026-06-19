from typing import Optional
from pydantic import BaseModel

class CreateClientDTO(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    company: str 
    location: str

class ClientDTO(BaseModel):
    id: int
    firstname: Optional[str]
    lastname: Optional[str]
    company: str
    location: str
