import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
_database_url = os.getenv("URL")
if _database_url is None:
    raise ValueError("Database URL is missing !")

engine = create_engine(
    _database_url,
    echo=True,
    connect_args={"options": f"-csearch_path={os.getenv('POSTGRES_SCHEMA')}"},
)
