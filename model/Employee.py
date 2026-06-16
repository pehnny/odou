from typing import Optional, TYPE_CHECKING
from sqlalchemy import Identity, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model import BaseAgenda

if TYPE_CHECKING:
    from model import Team, Role

class Employee(BaseAgenda):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    team_id: Mapped[Optional[int]] = mapped_column(ForeignKey("agenda.teams.id", onupdate="CASCADE", ondelete="SET NULL"))
    role_id: Mapped[Optional[int]] = mapped_column(ForeignKey("agenda.roles.id", onupdate="CASCADE", ondelete="SET NULL"))

    team: Mapped[Optional["Team"]] = relationship(back_populates="employees")
    role: Mapped[Optional["Role"]] = relationship(back_populates="employees")
