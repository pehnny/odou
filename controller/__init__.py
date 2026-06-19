from .home import router as home
from .employee.employee import router as employee
from .team.team import router as team

__all__ = [
    "home",
    "employee",
    "team",
]