from typing import Optional
from fastapi import APIRouter
from repository import TeamRepository, EmployeeRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateTeamDTO, TeamDTO, EmployeeDTO

router = APIRouter()

@router.get("/team")
def get_all() -> Optional[list[TeamDTO]]:
    with Session(engine) as session:
        try:
            teams = TeamRepository.select_all(session)
        except:
            return None
    return teams

@router.get("/team/{team_id}")
def get_team_by_id(team_id: int) -> Optional[TeamDTO]:
    with Session(engine) as session:
        try:
            team = TeamRepository.get_by_id(session, team_id)
        except:
            return None
    return team

@router.post("/team")
def create_new_team(body: CreateTeamDTO) -> Optional[TeamDTO]:
    with Session(engine) as session:
        try:
            team = TeamRepository.insert_new(session, body)
            session.commit()
        except:
            session.rollback()
            return None
    return team

@router.delete("/team/{team_id}")
def delete_team(team_id: int) -> bool:
    with Session(engine) as session:
        try:
            TeamRepository.delete_by_id(session, team_id)
            session.commit()
        except:
            session.rollback()
            return False
    return True
