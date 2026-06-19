from .home import router as home
from .employee.employee import router as employee
from .team.team import router as team
from .role.role import router as role
from .client.client import router as client

__all__ = [
    "home",
    "employee",
    "team",
    "role",
    "client",
]