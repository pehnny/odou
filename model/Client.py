from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from sqlalchemy import Identity
from model import BaseAgenda
if TYPE_CHECKING:
    from model import Mission

class Client(BaseAgenda, table=True):
    __tablename__ = "clients"

    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"server_default": Identity(always=True)})
    firstname: Optional[str]
    lastname: Optional[str]
    company: Optional[str]
    location: Optional[str]

    missions: list["Mission"] = Relationship(back_populates="client")