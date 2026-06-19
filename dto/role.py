from pydantic import BaseModel

class CreateRoleDTO(BaseModel):
    name: str

class RoleDTO(BaseModel):
    id: int
    name: str
