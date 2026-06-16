from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from sqlalchemy import Identity, ForeignKey, Column, Integer, ForeignKeyConstraint
from model import BaseAgenda
if TYPE_CHECKING:
    from model import Employee, Schedule

class Team(BaseAgenda, table=True):
    __tablename__ = "teams"

    id: Optional[int] = Field(
        default=None, 
        primary_key=True, 
        sa_column_kwargs={"server_default": Identity(always=True)}
    )
    leader_id: Optional[int] = Field(default=None)

    employees: list["Employee"] = Relationship(back_populates="team_id")
    leader: Optional["Employee"] = Relationship(back_populates="team_leader")
    schedules: list["Schedule"] = Relationship(back_populates="team")

    __table_args__ = (
        ForeignKeyConstraint(["leader_id"], ["agenda.employees.id"], onupdate="CASCADE", ondelete="SET NULL"),
        BaseAgenda.__table_args__
    )