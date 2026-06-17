from typing import Optional
from fastapi import APIRouter
from repository import EmployeeRepository, TeamRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateEmployeeDTO, EmployeeDTO

router = APIRouter()

@router.get("/employee/{employee_id}", response_model=EmployeeDTO)
def get_employee_by_id(employee_id: int) -> Optional[EmployeeDTO]:
    with Session(engine) as session:
        try:
            employee = EmployeeRepository.get_by_id(session, employee_id)
        except:
            return None
    return employee

@router.post("/employee/hire", response_model=EmployeeDTO)
def hire_new_employee(body: CreateEmployeeDTO) -> Optional[EmployeeDTO]:
    with Session(engine) as session:
        try:
            employee = EmployeeRepository.create(session, body)
            session.commit()
        except:
            session.rollback()
            return None
    return employee

@router.delete("/employee/{employee_id}")
def fire_employee(employee_id: int) -> bool:
    with Session(engine) as session:
        try:
            EmployeeRepository.delete_by_id(session, employee_id)
            session.commit()
        except:
            session.rollback()
            return False
    return True

@router.patch("/employee/{emmployee_id}/team/{team_id}")
def change_employee_team(employee_id: int, team_id: int) -> Optional[EmployeeDTO]:
    with Session(engine) as session:
        try:
            team = TeamRepository.exist(session, team_id)
            print("*******************", team)
            if not team:
                raise ValueError("Team does not exist !")
            employee = EmployeeRepository.update_team(session, employee_id, team_id)
            session.commit()
        except:
            session.rollback()
            return None
    return employee