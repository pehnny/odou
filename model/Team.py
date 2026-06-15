from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Identity
if TYPE_CHECKING:
    from model import Employee, Schedule

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"server_default": Identity(always=True)})
    leader_id: Optional[int] = Field(default=None, foreign_key="employee.id")

    employees: list["Employee"] = Relationship(back_populates="team_id")
    leader: Optional["Employee"] = Relationship(back_populates="team_leader")
    schedules: list["Schedule"] = Relationship(back_populates="team")