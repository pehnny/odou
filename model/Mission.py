from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from sqlalchemy import Identity, ForeignKey, Column, Integer, ForeignKeyConstraint
from model import BaseAgenda
if TYPE_CHECKING:
    from model import Client, Schedule

class Mission(BaseAgenda, table=True):
    __tablename__ = "missions"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"server_default": Identity(always=True)}
    )
    mission: str
    client_id: Optional[int] = Field(default=None)

    client: Optional["Client"] = Relationship(back_populates="missions")
    schedule: Optional["Schedule"] = Relationship(back_populates="mission")

    __table_args__ = (
        ForeignKeyConstraint(["client_id"], ["agenda.clients.id"], onupdate="CASCADE", ondelete="CASCADE"),
        BaseAgenda.__table_args__
    )