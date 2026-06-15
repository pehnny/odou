from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Identity
if TYPE_CHECKING:
    from model import Mission

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"server_default": Identity(always=True)})
    firstname: Optional[str]
    lastname: Optional[str]
    company: Optional[str]
    location: Optional[str]

    missions: list["Mission"] = Relationship(back_populates="client")