from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from sqlalchemy import Identity, ForeignKey, Column, Integer,ForeignKeyConstraint
from model import BaseAgenda
if TYPE_CHECKING:
    from model import Team, Mission

class Schedule(BaseAgenda, table=True):
    __tablename__ = "schedules"

    id: Optional[int] = Field(
        default=None, 
        primary_key=True, 
        sa_column_kwargs={"server_default": Identity(always=True)}
    )
    start_date: datetime = Field(nullable=False)
    end_date: datetime= Field(nullable=False)
    team_id: int = Field(default=None)
    mission_id: int = Field(default=None)

    team: Optional["Team"] = Relationship(back_populates="schedules")
    mission: Optional["Mission"] = Relationship(back_populates="schedule")
    
    __table_args__ = (
        ForeignKeyConstraint(["team_id"], ["agenda.teams.id"], onupdate="CASCADE", ondelete="CASCADE"),
        ForeignKeyConstraint(["mission_id"], ["agenda.missions.id"], onupdate="CASCADE", ondelete="CASCADE"),
        BaseAgenda.__table_args__
    )