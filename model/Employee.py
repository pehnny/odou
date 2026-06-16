from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from sqlalchemy import Identity, ForeignKeyConstraint
from model import BaseAgenda
if TYPE_CHECKING:
    from model import Team, Role

class Employee(BaseAgenda, table=True):
    __tablename__ = "employees"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"server_default": Identity(always=True)}
    )
    firstname: str
    lastname: str
    team_id: Optional[int] = Field(default=None)
    role_id: Optional[int] = Field(default=None)

    team: Optional["Team"] = Relationship(back_populates="employees")
    team_leader: Optional["Team"] = Relationship(back_populates="team_leader")
    role: Optional["Role"] = Relationship(back_populates="employees")

    __table_args__ = (
        ForeignKeyConstraint(["team_id"], ["agenda.teams.id"], onupdate="CASCADE", ondelete="SET NULL"),
        ForeignKeyConstraint(["role_id"], ["agenda.roles.id"], onupdate="CASCADE", ondelete="SET NULL"),
        BaseAgenda.__table_args__
    )