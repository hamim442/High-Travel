from pydantic import BaseModel
from datetime import datetime


class Flight(BaseModel):
    id: int
    flight_number: str
    departure_time: datetime
    arrival_time: datetime
    departure_airport: str
    arrival_airport: str
    price: int
    airline_id: int
    trip_id: int


class FlightRequest(BaseModel):
    flight_number: str
    departure_time: datetime
    arrival_time: datetime
    departure_airport: str
    arrival_airport: str
    price: int
    airline_id: int
    trip_id: int
