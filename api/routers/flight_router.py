from fastapi import APIRouter, Depends, HTTPException
from queries.flight_queries import (
    FlightQueries,
    FlightDoesNotExist,
    FlightDatabaseError,
    FlightCreationError,
)
from models.flights import Flight, FlightRequest


router = APIRouter(tags=["Flight"], prefix="/api/flights")


@router.get("/")
async def get_all_flights(
    queries: FlightQueries = Depends(),
) -> list[Flight]:
    try:
        flights = queries.get_all_flights()
        return flights
    except FlightDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve flights."
        )


@router.get("/{id}")
def get_flight(id: int, queries: FlightQueries = Depends()) -> Flight:
    try:
        flight = queries.get_flight(id)
        return flight
    except FlightDoesNotExist:
        raise HTTPException(status_code=404, detail="Flight not found")
    except FlightDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve flights."
        )


@router.post("/")
def create_flight(
    flight: FlightRequest, queries: FlightQueries = Depends()
) -> Flight:
    try:
        new_flight = queries.create_flight(flight)
        return new_flight
    except FlightCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except FlightDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
