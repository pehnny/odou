from fastapi import FastAPI
from controller import home

app = FastAPI()
app.include_router(home)