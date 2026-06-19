from typing import Optional
from sqlalchemy import select, delete, insert, exists
from sqlalchemy.orm import Session
from model import Client

class ClientRepository:
    @staticmethod
    def select_all(session: Session) -> Optional[list[Client]]:
        query = select(Client).order_by(Client.id)
        clients = session.execute(query).scalars().all()
        return list(clients)

    @staticmethod
    def exist(session: Session, client_id: int) -> bool:
        query = select(exists(Client).where(Client.id == client_id))
        result = session.execute(query).scalar_one()
        return result

    @staticmethod
    def get_by_id(session: Session, client_id: int) -> Optional[Client]:
        query = select(Client).where(Client.id == client_id)
        client = session.execute(query).scalar_one_or_none()
        return client

    @staticmethod
    def insert_new(session: Session, data) -> Optional[Client]:
        query = insert(Client).values(
            firstname=data.firstname,
            lastname=data.lastname,
            company=data.company,
            location=data.location
        )
        client = session.execute(query).scalar_one_or_none()
        session.flush()
        return client

    @staticmethod
    def delete_by_id(session: Session, client_id: int) -> None:
        query = delete(Client).where(Client.id == client_id)
        session.execute(query)
        session.flush()
        return
