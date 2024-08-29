from pydantic import BaseModel
from datetime import datetime


class UserTripRequest(BaseModel):
    user_id: int
    trip_id: int


class UserTripResponse(BaseModel):
    user_id: int
    trip_id: int


class TripByUserResponse(BaseModel):
    trip_id: int
    start_date: datetime
    end_date: datetime
    city_name: str
    city_picture_url: str
    country_name: str
