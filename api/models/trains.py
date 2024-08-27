from pydantic import BaseModel
from datetime import datetime

class Train(BaseModel):
    id: int
    train_number: str
    departure_time: datetime
    arrival_time: datetime
    departure_station: str
    arrival_station: str
    price: int
    trip_id: int

class TrainRequest(BaseModel):
    train_number: str
    departure_time: datetime
    arrival_time: datetime
    departure_station: str
    arrival_station: str
    price: int
    trip_id: int
