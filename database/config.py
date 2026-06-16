import os
from sqlmodel import create_engine
from dotenv import load_dotenv

load_dotenv()
_dabatabase_url = os.getenv("URL")
engine = create_engine(
    _dabatabase_url,
    echo=True,
    connect_args={"options": f"-csearch_path={os.getenv("POSTGRES_SCHEMA")}"}
)