from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Identity
if TYPE_CHECKING:
    from model import Team, Role

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"server_default": Identity(always=True)})
    firstname: str
    lastname: str
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")

    team: Optional["Team"] = Relationship(back_populates="employees")
    team_leader: Optional["Team"] = Relationship(back_populates="team_leader")
    role: Optional["Role"] = Relationship(back_populates="employee")