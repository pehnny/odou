from typing import Optional
from fastapi import APIRouter
from repository import ClientRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateClientDTO, ClientDTO

router = APIRouter()

@router.get("/client")
def get_all() -> Optional[list[ClientDTO]]:
    with Session(engine) as session:
        try:
            clients = ClientRepository.select_all(session)
        except:
            return None
    return clients

@router.get("/client/{client_id}")
def get_client_by_id(client_id: int) -> Optional[ClientDTO]:
    with Session(engine) as session:
        try:
            client = ClientRepository.get_by_id(session, client_id)
        except:
            return None
    return client

@router.post("/client")
def create_new_client(body: CreateClientDTO) -> Optional[ClientDTO]:
    with Session(engine) as session:
        try:
            client = ClientRepository.insert_new(session, body)
            session.commit()
        except:
            session.rollback()
            return None
    return client

@router.delete("/client/{client_id}")
def delete_client(client_id: int) -> bool:
    with Session(engine) as session:
        try:
            ClientRepository.delete_by_id(session, client_id)
            session.commit()
        except:
            session.rollback()
            return False
    return True
