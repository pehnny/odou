from typing import Optional
from sqlalchemy import select, delete, insert, exists
from sqlalchemy.orm import Session
from model import Mission

class MissionRepository:
    @staticmethod
    def select_all(session: Session) -> Optional[list[Mission]]:
        query = select(Mission).order_by(Mission.id)
        missions = session.execute(query).scalars().all()
        return list(missions)

    @staticmethod
    def exist(session: Session, mission_id: int) -> bool:
        query = select(exists(Mission).where(Mission.id == mission_id))
        result = session.execute(query).scalar_one()
        return result

    @staticmethod
    def get_by_id(session: Session, mission_id: int) -> Optional[Mission]:
        query = select(Mission).where(Mission.id == mission_id)
        mission = session.execute(query).scalar_one_or_none()
        return mission

    @staticmethod
    def insert_new(session: Session, data) -> Optional[Mission]:
        query = insert(Mission).values(
            name=data.name,
            client_id=data.client_id
        )
        mission = session.execute(query).scalar_one_or_none()
        session.flush()
        return mission

    @staticmethod
    def select_missions_by_client(session: Session, client) -> Optional[list[Mission]]:
        return client.missions

    @staticmethod
    def delete_by_id(session: Session, mission_id: int) -> None:
        query = delete(Mission).where(Mission.id == mission_id)
        session.execute(query)
        session.flush()
        return
