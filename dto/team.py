from pydantic import BaseModel

class CreateTeamDTO(BaseModel):
    name: str

class TeamDTO(BaseModel):
    id: int
    name: str
