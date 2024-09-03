from pydantic import BaseModel
from datetime import datetime
from typing import Optional


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


class AccommodationUpdate(BaseModel):
    stays_id: Optional[int] | None
    address: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    check_in_date: Optional[datetime] = None
    check_out_date: Optional[datetime] = None
    number_of_guests: Optional[int] | None
    total_price: Optional[float] = None
    notes: Optional[str] = None
    trip_id: Optional[int] | None
