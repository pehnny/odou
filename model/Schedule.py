from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import BaseAgenda

if TYPE_CHECKING:
    from model import Team, Mission

class Schedule(BaseAgenda):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    team_id: Mapped[int] = mapped_column(ForeignKey("agenda.teams.id", onupdate="CASCADE", ondelete="CASCADE"))
    mission_id: Mapped[int] = mapped_column(ForeignKey("agenda.missions.id", onupdate="CASCADE", ondelete="CASCADE"))

    team: Mapped[Optional["Team"]] = relationship(back_populates="schedules")
    mission: Mapped[Optional["Mission"]] = relationship(back_populates="schedules")

    __table_args__ = (
        CheckConstraint("start_date < end_date", name="ck_schedule_dates"),
        BaseAgenda.__table_args__,
    )
