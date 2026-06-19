from typing import Optional
from fastapi import APIRouter
from repository import ScheduleRepository, TeamRepository, MissionRepository, ClientRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateScheduleDTO, ScheduleDTO

router = APIRouter()

@router.get("/schedule")
def get_all() -> Optional[list[ScheduleDTO]]:
    with Session(engine) as session:
        try:
            schedules = ScheduleRepository.select_all(session)
        except:
            return None
    return schedules

@router.get("/schedule/{schedule_id}")
def get_schedule_by_id(schedule_id: int) -> Optional[ScheduleDTO]:
    with Session(engine) as session:
        try:
            schedule = ScheduleRepository.get_by_id(session, schedule_id)
        except:
            return None
    return schedule

@router.post("/schedule")
def create_new_schedule(body: CreateScheduleDTO) -> Optional[ScheduleDTO]:
    with Session(engine) as session:
        try:
            schedule = ScheduleRepository.insert_new(session, body)
            session.commit()
        except:
            session.rollback()
            return None
    return schedule

@router.delete("/schedule/{schedule_id}")
def delete_schedule(schedule_id: int) -> bool:
    with Session(engine) as session:
        try:
            ScheduleRepository.delete_by_id(session, schedule_id)
            session.commit()
        except:
            session.rollback()
            return False
    return True

@router.get("/schedule/team/{team_id}")
def get_schedules_by_team(team_id: int) -> Optional[list[ScheduleDTO]]:
    with Session(engine) as session:
        try:
            team = TeamRepository.get_by_id(session, team_id)
            if team is None:
                return None
            schedules = ScheduleRepository.select_schedules_by_team(session, team)
        except:
            return None
    return schedules

@router.get("/schedule/mission/{mission_id}")
def get_schedules_by_mission(mission_id: int) -> Optional[list[ScheduleDTO]]:
    with Session(engine) as session:
        try:
            mission = MissionRepository.get_by_id(session, mission_id)
            if mission is None:
                return None
            schedules = ScheduleRepository.select_schedules_by_mission(session, mission)
        except:
            return None
    return schedules

@router.get("/schedule/client/{client_id}")
def get_schedules_by_client(client_id: int) -> Optional[list[ScheduleDTO]]:
    with Session(engine) as session:
        try:
            is_client = ClientRepository.exist(session, client_id)
            if not is_client:
                return None
            schedules = ScheduleRepository.select_schedules_by_client(session, client_id)
        except:
            return None
    return schedules
