from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Identity
if TYPE_CHECKING:
    from model import Client, Schedule

class Mission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"server_default": Identity(always=True)})
    mission: str
    client_id: Optional[int] = Field(default=None, foreign_key="mission.id")

    client: Optional["Client"] = Relationship(back_populates="missions")
    schedule: Optional["Schedule"] = Relationship(back_populates="mission")