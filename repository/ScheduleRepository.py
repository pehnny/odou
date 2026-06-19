from typing import Optional
from sqlalchemy import select, delete, insert, exists
from sqlalchemy.orm import Session
from model import Schedule, Mission

class ScheduleRepository:
    @staticmethod
    def select_all(session: Session) -> Optional[list[Schedule]]:
        query = select(Schedule).order_by(Schedule.id)
        schedules = session.execute(query).scalars().all()
        return list(schedules)

    @staticmethod
    def exist(session: Session, schedule_id: int) -> bool:
        query = select(exists(Schedule).where(Schedule.id == schedule_id))
        result = session.execute(query).scalar_one()
        return result

    @staticmethod
    def get_by_id(session: Session, schedule_id: int) -> Optional[Schedule]:
        query = select(Schedule).where(Schedule.id == schedule_id)
        schedule = session.execute(query).scalar_one_or_none()
        return schedule

    @staticmethod
    def insert_new(session: Session, data) -> Optional[Schedule]:
        query = insert(Schedule).values(
            start_date=data.start_date,
            end_date=data.end_date,
            team_id=data.team_id,
            mission_id=data.mission_id
        )
        schedule = session.execute(query).scalar_one_or_none()
        session.flush()
        return schedule

    @staticmethod
    def select_schedules_by_team(session: Session, team) -> Optional[list[Schedule]]:
        return team.schedules

    @staticmethod
    def select_schedules_by_mission(session: Session, mission) -> Optional[list[Schedule]]:
        return mission.schedules

    @staticmethod
    def select_schedules_by_client(session: Session, client_id: int) -> Optional[list[Schedule]]:
        query = select(Schedule).join(Mission).where(Mission.client_id == client_id).order_by(Schedule.id)
        schedules = session.execute(query).scalars().all()
        return list(schedules)

    @staticmethod
    def delete_by_id(session: Session, schedule_id: int) -> None:
        query = delete(Schedule).where(Schedule.id == schedule_id)
        session.execute(query)
        session.flush()
        return
