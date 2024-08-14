from pydantic import BaseModel
from datetime import datetime


class Accommodation(BaseModel):
    id: int
    stays_id: int | None
    address: str
    city: str
    state_province: str | None
    zip_code: str
    country: str
    phone: str | None
    email: str | None
    check_in_date: datetime
    check_out_date: datetime
    number_of_guests: int
    total_price: float
    notes: str | None
    trip_id: int


class AccommodationRequest(BaseModel):
    stays_id: int | None
    address: str
    city: str
    state_province: str | None
    zip_code: str
    country: str
    phone: str | None
    email: str | None
    check_in_date: datetime
    check_out_date: datetime
    number_of_guests: int
    total_price: float
    notes: str | None
    trip_id: int
