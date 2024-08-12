from fastapi import APIRouter, Depends, HTTPException
from queries.airline_queries import (
    AirlineQueries,
)  # import Error Case when they're working well
from models.airlines import Airline, AirlineRequest

router = APIRouter(tags=["Airline"], prefix="/api/airlines")


@router.get("/")
async def get_all_airlines(
    queries: AirlineQueries = Depends(),
) -> list[Airline]:
    airlines = queries.get_all_airlines()
    return airlines


@router.get("/{id}")
def get_airline(id: int, queries: AirlineQueries = Depends()) -> Airline:
    airline = queries.get_airline(id)
    if airline is None:
        raise HTTPException(status_code=404, detail="Airline not found.")
    return airline
