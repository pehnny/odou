from fastapi import APIRouter
from repository import EmployeeRepository
from database import engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

@router.get("/employee/{id}")
def get_employee_by_id(employee_id: int) -> Employee:
    with sessionmaker(engine) as session :
        employee = EmployeeRepository.get_by_id(session, employee_id)
    return employee