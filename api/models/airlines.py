from pydantic import BaseModel


class Airline(BaseModel):
    id: int
    name: str
    logo_picture_url: str


class AirlineRequest(BaseModel):
    name: str
    logo_picture_url: str
