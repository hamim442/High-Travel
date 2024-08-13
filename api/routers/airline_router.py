from fastapi import APIRouter, Depends, HTTPException
from queries.airline_queries import (
    AirlineQueries,
    AirlineDoesNotExist,
    AirlineDatabaseError,
    AirlineCreationError,
)
from models.airlines import Airline, AirlineRequest

router = APIRouter(tags=["Airline"], prefix="/api/airlines")


@router.get("/")
async def get_all_airlines(
    queries: AirlineQueries = Depends(),
) -> list[Airline]:
    try:
        airlines = queries.get_all_airlines()
        return airlines
    except AirlineDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve airlines."
        )


@router.get("/{id}")
def get_airline(id: int, queries: AirlineQueries = Depends()) -> Airline:
    try:
        airline = queries.get_airline(id)
        return airline
    except AirlineDoesNotExist:
        raise HTTPException(status_code=404, detail="Airline not found.")
    except AirlineDatabaseError:
        raise HTTPException(
            status_code=500, detail="Error retrieving airline."
        )


@router.post("/")
def create_airline(
    airline: AirlineRequest, queries: AirlineQueries = Depends()
) -> Airline:
    try:
        new_airline = queries.create_airline(airline)
        return new_airline
    except AirlineCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except AirlineDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
