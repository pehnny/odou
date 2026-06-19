from typing import Optional
from sqlalchemy import select, delete, insert, exists
from sqlalchemy.orm import Session
from model import Role

class RoleRepository:
    @staticmethod
    def select_all(session: Session) -> Optional[list[Role]]:
        query = select(Role).order_by(Role.id)
        roles = session.execute(query).scalars().all()
        return list(roles)

    @staticmethod
    def exist(session: Session, role_id: int) -> bool:
        query = select(exists(Role).where(Role.id == role_id))
        result = session.execute(query).scalar_one()
        return result

    @staticmethod
    def get_by_id(session: Session, role_id: int) -> Optional[Role]:
        query = select(Role).where(Role.id == role_id)
        role = session.execute(query).scalar_one_or_none()
        return role

    @staticmethod
    def insert_new(session: Session, data) -> Optional[Role]:
        name = data.name
        query = insert(Role).values(name=name)
        role = session.execute(query).scalar_one_or_none()
        session.flush()
        return role

    @staticmethod
    def delete_by_id(session: Session, role_id: int) -> None:
        query = delete(Role).where(Role.id == role_id)
        session.execute(query)
        session.flush()
        return
