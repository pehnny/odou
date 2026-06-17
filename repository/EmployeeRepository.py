from typing import Optional
from sqlalchemy import select, delete, insert, update
from sqlalchemy.orm import Session
from model import Employee
from dto import CreateEmployeeDTO

class EmployeeRepository:
    @staticmethod
    def get_by_id(session: Session, employee_id: int) -> Optional[Employee]:
        query = select(Employee).where(Employee.id == employee_id)
        employee = session.execute(query).scalar()
        return employee
    
    @staticmethod
    def create(session: Session, data: CreateEmployeeDTO) -> Optional[Employee]:
        firstname = data.firstname
        lastname = data.lastname
        employee = Employee(firstname=firstname, lastname=lastname)
        query = insert(Employee).values(firstname=firstname, lastname=lastname)
        employee = session.execute(query).scalar()
        session.flush()
        return employee
    
    @staticmethod
    def delete_by_id(session: Session, employee_id: int) -> None:
        query = delete(Employee).where(Employee.id == employee_id)
        session.execute(query)
        session.flush()
        return
    
    @staticmethod
    def update_team(session: Session, employee_id: int, team_id: int) -> Optional[Employee]:
        query = update(Employee).where(Employee.id == employee_id).values(team_id=team_id)
        employee = session.execute(query)
        session.flush()
        return employee