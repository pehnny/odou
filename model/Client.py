from typing import Optional, TYPE_CHECKING
from sqlalchemy import Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model import BaseAgenda

if TYPE_CHECKING:
    from model import Mission

class Client(BaseAgenda):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    firstname: Mapped[Optional[str]]
    lastname: Mapped[Optional[str]]
    company: Mapped[str]
    location: Mapped[str]

    missions: Mapped[list["Mission"]] = relationship(back_populates="client")
