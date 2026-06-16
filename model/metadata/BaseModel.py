from sqlmodel import SQLModel
import os
from dotenv import load_dotenv

load_dotenv()

class BaseAgenda(SQLModel):
    __table_args__ = {"schema": os.getenv("POSTGRES_SCHEMA")}