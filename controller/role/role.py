from typing import Optional
from fastapi import APIRouter
from repository import RoleRepository
from database import engine
from sqlalchemy.orm import Session
from dto import CreateRoleDTO, RoleDTO

router = APIRouter()

@router.get("/role")
def get_all() -> Optional[list[RoleDTO]]:
    with Session(engine) as session:
        try:
            roles = RoleRepository.select_all(session)
        except:
            return None
    return roles

@router.get("/role/{role_id}")
def get_role_by_id(role_id: int) -> Optional[RoleDTO]:
    with Session(engine) as session:
        try:
            role = RoleRepository.get_by_id(session, role_id)
        except:
            return None
    return role

@router.post("/role")
def create_new_role(body: CreateRoleDTO) -> Optional[RoleDTO]:
    with Session(engine) as session:
        try:
            role = RoleRepository.insert_new(session, body)
            session.commit()
        except:
            session.rollback()
            return None
    return role

@router.delete("/role/{role_id}")
def delete_role(role_id: int) -> bool:
    with Session(engine) as session:
        try:
            RoleRepository.delete_by_id(session, role_id)
            session.commit()
        except:
            session.rollback()
            return False
    return True
