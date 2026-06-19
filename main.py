from datetime import datetime
from database import engine
from seed import init_seed
from sqlalchemy.orm import Session
from fastapi import FastAPI
from controller import home, employee, team, role, client
from pathlib import Path
import traceback
from database import engine

path = Path(__file__).parent.joinpath("error/").joinpath("logs.txt")
path.touch()

with Session(engine) as session:
    try:
        init_seed(session)
        print("Seed terminée.")
    except:
        session.rollback()
        traceback.print_exc()
        with open(path, "a") as file:
            file.write("########" + str(datetime.now()) + "\n")
            file.write(traceback.format_exc() + "\n")

app = FastAPI()
app.include_router(home)
app.include_router(employee)
app.include_router(team)
app.include_router(role)
app.include_router(client)
