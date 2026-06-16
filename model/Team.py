from typing import TYPE_CHECKING

from sqlalchemy import Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import BaseAgenda

if TYPE_CHECKING:
    from model import Employee, Schedule

class Team(BaseAgenda):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str]

    employees: Mapped[list["Employee"]] = relationship(back_populates="team")
    schedules: Mapped[list["Schedule"]] = relationship(back_populates="team")
