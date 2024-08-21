from pydantic import BaseModel


class City(BaseModel):
    id: int
    name: str
    administrative_division: str | None
    country: str
    picture_url: str
    description: str | None


class CityRequest(BaseModel):
    name: str
    administrative_division: str | None
    country: str
    picture_url: str
    description: str | None
