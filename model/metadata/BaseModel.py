from datetime import datetime
import os

from dotenv import load_dotenv
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()
_schema = os.getenv("POSTGRES_SCHEMA")
if _schema is None:
    raise ValueError("Database schema is missing !")

class BaseAgenda(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {"schema": _schema}

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
