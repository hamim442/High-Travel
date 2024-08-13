from fastapi import APIRouter, Depends, HTTPException
from queries.trip_queries import (
    TripQueries,
    TripDoesNotExist,
    TripDatabaseError,
    TripCreationError,
)
from models.trips import Trip, TripRequest

router = APIRouter(tags=["Trip"], prefix="/api/trips")


@router.get("/")
async def get_all_trips(
    queries: TripQueries = Depends(),
) -> list[Trip]:
    try:
        trips = queries.get_all_trips()
        return trips
    except TripDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve trips."
        )


@router.get("/{id}")
def get_trip(id: int, queries: TripQueries = Depends()) -> Trip:
    try:
        trip = queries.get_trip(id)
        return trip
    except TripDoesNotExist:
        raise HTTPException(status_code=404, detail="Trip not found.")
    except TripDatabaseError:
        raise HTTPException(status_code=500, detail="Error retrieving trip.")


@router.post("/")
def create_trip(trip: TripRequest, queries: TripQueries = Depends()) -> Trip:
    try:
        new_trip = queries.create_trip(trip)
        return new_trip
    except TripCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TripDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
