from pydantic import BaseModel
from datetime import datetime


class Trip(BaseModel):
    id: int
    city_id: int | None
    start_date: datetime
    end_date: datetime
    user_id: int


class TripRequest(BaseModel):
    city_id: int | None
    start_date: datetime
    end_date: datetime
