from typing import Optional
from fastapi import APIRouter
from repository import EmployeeRepository, TeamRepository, RoleRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateEmployeeDTO, EmployeeDTO
import traceback

router = APIRouter()

@router.get("/employee")
def get_all() -> Optional[list[EmployeeDTO]]:
    with Session(engine) as session:
        try:
            employees = EmployeeRepository.select_all(session)
        except:
            return None
    return employees


@router.get("/employee/{employee_id}")
def get_employee_by_id(employee_id: int) -> Optional[EmployeeDTO]:
    with Session(engine) as session:
        try:
            employee = EmployeeRepository.select_by_id(session, employee_id)
        except:
            return None
    return employee

@router.post("/employee/hire")
def hire_new_employee(body: CreateEmployeeDTO) -> Optional[EmployeeDTO]:
    with Session(engine) as session:
        try:
            employee = EmployeeRepository.insert_new(session, body)
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

@router.patch("/employee/{employee_id}/team/{team_id}")
def change_employee_team(employee_id: int, team_id: int) -> Optional[EmployeeDTO]:
    response = None
    with Session(engine) as session:
        try:
            is_team = TeamRepository.exist(session, team_id)
            if not is_team:
                raise ValueError("Team does not exist !")
            
            employee = EmployeeRepository.update_team(session, employee_id, team_id)
            if employee is None:
                raise TypeError("Employee not found !")
            
            response = EmployeeDTO.model_validate(employee, from_attributes=True)
            session.commit()
        except:
            traceback.print_exc()
            session.rollback()
            return
    return response

@router.patch("/employee/{employee_id}/role/{role_id}")
def change_employee_role(employee_id: int, role_id: int) -> Optional[EmployeeDTO]:
    response = None
    with Session(engine) as session:
        try:
            is_role = RoleRepository.exist(session, role_id)
            if not is_role:
                raise ValueError("Role does not exist !")
            
            employee = EmployeeRepository.update_role(session, employee_id, role_id)
            if employee is None:
                raise TypeError("Employee not found !")
            
            response = EmployeeDTO.model_validate(employee, from_attributes=True)
            session.commit()
        except:
            traceback.print_exc()
            session.rollback()
            return
    return response

@router.get("/employee/team/{team_id}")
def get_employee_by_team_id(team_id: int) -> Optional[list[EmployeeDTO]]:
    with Session(engine) as session:
        try:
            team = TeamRepository.get_by_id(session, team_id)
            if team is None:
                return None
            members = EmployeeRepository.select_employees_by_team(session, team)
        except:
            return None
    return members

@router.get("/employee/role/{role_id}")
def get_employee_by_role_id(role_id: int) -> Optional[list[EmployeeDTO]]:
    with Session(engine) as session:
        try:
            role = TeamRepository.get_by_id(session, role_id)
            if role is None:
                return None
            members = EmployeeRepository.select_employees_by_role(session, role)
        except:
            return None
    return members
