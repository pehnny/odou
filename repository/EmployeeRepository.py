from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from model import Employee

class EmployeeRepository:
    @staticmethod
    def get_by_id(session: Session, employee_id: int) -> Optional[Employee]:
        query = select(Employee).where(Employee.id == employee_id)
        employee = session.execute(query).scalar()
        return employee