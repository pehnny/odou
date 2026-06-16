from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from sqlalchemy import Identity
from model import BaseAgenda
if TYPE_CHECKING:
    from model import Employee

class Role(BaseAgenda, table=True):
    __tablename__ = "roles"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"server_default": Identity(always=True)}
    )
    role: str

    employees: list["Employee"] = Relationship(back_populates="role")