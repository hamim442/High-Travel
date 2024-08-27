from pydantic import BaseModel
from datetime import datetime

class Car(BaseModel):
    id: int
    car_model: str
    rental_company: str
    pickup_time: datetime
    dropoff_time: datetime
    pickup_location: str
    dropoff_location: str
    price: int
    trip_id: int

class CarRequest(BaseModel):
    car_model: str
    rental_company: str
    pickup_time: datetime
    dropoff_time: datetime
    pickup_location: str
    dropoff_location: str
    price: int
    trip_id: int
