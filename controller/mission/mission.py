from typing import Optional
from fastapi import APIRouter
from repository import MissionRepository, ClientRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateMissionDTO, MissionDTO

router = APIRouter()

@router.get("/mission")
def get_all() -> Optional[list[MissionDTO]]:
    with Session(engine) as session:
        try:
            missions = MissionRepository.select_all(session)
        except:
            return None
    return missions

@router.get("/mission/{mission_id}")
def get_mission_by_id(mission_id: int) -> Optional[MissionDTO]:
    with Session(engine) as session:
        try:
            mission = MissionRepository.get_by_id(session, mission_id)
        except:
            return None
    return mission

@router.post("/mission")
def create_new_mission(body: CreateMissionDTO) -> Optional[MissionDTO]:
    with Session(engine) as session:
        try:
            mission = MissionRepository.insert_new(session, body)
            session.commit()
        except:
            session.rollback()
            return None
    return mission

@router.delete("/mission/{mission_id}")
def delete_mission(mission_id: int) -> bool:
    with Session(engine) as session:
        try:
            MissionRepository.delete_by_id(session, mission_id)
            session.commit()
        except:
            session.rollback()
            return False
    return True

@router.get("/mission/client/{client_id}")
def get_missions_by_client(client_id: int) -> Optional[list[MissionDTO]]:
    with Session(engine) as session:
        try:
            client = ClientRepository.get_by_id(session, client_id)
            if client is None:
                return None
            missions = MissionRepository.select_missions_by_client(session, client)
        except:
            return None
    return missions
