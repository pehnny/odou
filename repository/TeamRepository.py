from typing import Optional
from sqlalchemy import select, delete, insert, exists
from sqlalchemy.orm import Session
from model import Team

class TeamRepository:
    @staticmethod
    def select_all(session: Session) -> Optional[list[Team]]:
        query = select(Team).order_by(Team.id)
        teams = session.execute(query).scalars().all()
        return list(teams)

    @staticmethod
    def exist(session: Session, team_id: int) -> bool:
        query = select(exists(Team).where(Team.id == team_id))
        result = session.execute(query).scalar_one()
        return result

    @staticmethod
    def get_by_id(session: Session, team_id: int) -> Optional[Team]:
        query = select(Team).where(Team.id == team_id)
        team = session.execute(query).scalar_one_or_none()
        return team

    @staticmethod
    def insert_new(session: Session, data) -> Optional[Team]:
        name = data.name
        query = insert(Team).values(name=name)
        team = session.execute(query).scalar_one_or_none()
        session.flush()
        return team

    @staticmethod
    def delete_by_id(session: Session, team_id: int) -> None:
        query = delete(Team).where(Team.id == team_id)
        session.execute(query)
        session.flush()
        return
