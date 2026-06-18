from typing import Optional
from sqlalchemy import select, delete, insert, update, exists
from sqlalchemy.orm import Session
from model import Employee
from dto import CreateEmployeeDTO

class EmployeeRepository:
    @staticmethod
    def select_all(session: Session) -> Optional[list[Employee]]:
        query = select(Employee).order_by(Employee.id)
        employees = session.execute(query).scalars().all()
        return list(employees)

    @staticmethod
    def exist(session: Session, employee_id: int) -> bool:
        query = select(exists(Employee).where(Employee.id == employee_id))
        result = session.execute(query).scalar_one()
        return result

    @staticmethod
    def select_by_id(session: Session, employee_id: int) -> Optional[Employee]:
        query = select(Employee).where(Employee.id == employee_id)
        employee = session.execute(query).scalar_one_or_none()
        return employee
    
    @staticmethod
    def insert_new(session: Session, data: CreateEmployeeDTO) -> Optional[Employee]:
        firstname = data.firstname
        lastname = data.lastname
        employee = Employee(firstname=firstname, lastname=lastname)
        query = insert(Employee).values(firstname=firstname, lastname=lastname)
        employee = session.execute(query).scalar_one_or_none()
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
        query = update(Employee).where(Employee.id == employee_id).values(team_id=team_id).returning(Employee)
        employee = session.execute(query).scalar_one_or_none()
        session.flush()
        return employee
    
    @staticmethod
    def update_role(session: Session, employee_id: int, role_id: int) -> Optional[Employee]:
        query = update(Employee).where(Employee.id == employee_id).values(role_id=role_id).returning(Employee)
        employee = session.execute(query).scalar_one_or_none()
        session.flush()
        return employee