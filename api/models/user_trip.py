from pydantic import BaseModel


class UserTripRequest(BaseModel):
    user_id: int
    trip_id: int


class UserTripResponse(BaseModel):
    user_id: int
    trip_id: int
