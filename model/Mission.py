from typing import Optional, TYPE_CHECKING

from sqlalchemy import Identity, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import BaseAgenda

if TYPE_CHECKING:
    from model import Client, Schedule

class Mission(BaseAgenda):
    __tablename__ = "missions"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str]
    client_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("agenda.clients.id", onupdate="CASCADE", ondelete="SET NULL")
    )

    client: Mapped[Optional["Client"]] = relationship(back_populates="missions")
    schedules: Mapped[list["Schedule"]] = relationship(back_populates="mission")
