from pydantic import BaseModel


class Stay(BaseModel):
    id: int
    name: str
    logo_picture_url: str


class StayRequest(BaseModel):
    name: str
    logo_picture_url: str
