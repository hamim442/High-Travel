from pydantic import BaseModel
from datetime import datetime


class Trip(BaseModel):
    id: int
    city_id: int | None
    start_date: datetime
    end_date: datetime


class TripRequest(BaseModel):
    city_id: int | None
    start_date: datetime
    end_date: datetime
