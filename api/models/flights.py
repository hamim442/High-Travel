from pydantic import BaseModel
from datetime import datetime


class Flight(BaseModel):
    id: int
    name: str
    description: str
    departure_time: datetime
    arrival_time: datetime
    departure_airport: str
    arrival_airport: str
    flight_number: int
    price: int
    airline_id: int
    trip_id: int


class FlightRequest(BaseModel):
    name: str
    description: str
    departure_time: datetime
    arrival_time: datetime
    departure_airport: str
    arrival_airport: str
    flight_number: int
    price: int
    airline_id: int
    trip_id: int
