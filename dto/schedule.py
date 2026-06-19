from datetime import datetime
from pydantic import BaseModel

class CreateScheduleDTO(BaseModel):
    start_date: datetime
    end_date: datetime
    team_id: int
    mission_id: int

class ScheduleDTO(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    team_id: int
    mission_id: int
