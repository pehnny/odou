from typing import TYPE_CHECKING

from sqlalchemy import Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import BaseAgenda

if TYPE_CHECKING:
    from model import Employee

class Role(BaseAgenda):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="role")
