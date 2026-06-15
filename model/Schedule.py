from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Identity
if TYPE_CHECKING:
    from model import Team, Mission

class Schedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"server_default": Identity(always=True)})
    start_date: datetime = Field(nullable=False)
    end_date: datetime= Field(nullable=False)
    team_id: int = Field(default=None, foreign_key="team.id", nullable=False)
    mission_id: int = Field(default=None, foreign_key="mission.id", nullable=False)

    team: Optional["Team"] = Relationship(back_populates="schedules")
    mission: Optional["Mission"] = Relationship(back_populates="schedule")