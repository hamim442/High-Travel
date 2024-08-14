from fastapi import APIRouter, Depends, HTTPException
from queries.trip_queries import (
    TripQueries,
    TripDoesNotExist,
    TripDatabaseError,
    TripCreationError,
)
from models.trips import Trip, TripRequest
from utils.authentication import try_get_jwt_user_data
from models.jwt import JWTUserData


router = APIRouter(tags=["Trip"], prefix="/api/trips")


# @router.get("/")
# async def get_all_trips(
#     queries: TripQueries = Depends(),
# ) -> list[Trip]:
#     try:
#         trips = queries.get_all_trips()
#         return trips
#     except TripDatabaseError:
#         raise HTTPException(
#             status_code=500, detail="Failed to retrieve trips."
#         )


@router.get("/")
async def get_user_trips(
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: TripQueries = Depends(),
) -> list[Trip]:
    try:
        trips = queries.get_user_trips(user.id)
        return trips
    except TripDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve trips."
        )


# @router.get("/{id}")
# def get_trip(id: int, queries: TripQueries = Depends()) -> Trip:
#     try:
#         trip = queries.get_trip(id)
#         return trip
#     except TripDoesNotExist:
#         raise HTTPException(status_code=404, detail="Trip not found.")
#     except TripDatabaseError:
#         raise HTTPException(status_code=500, detail="Error retrieving trip.")


@router.get("/{id}")
def get_trip(
    id: int,
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: TripQueries = Depends(),
) -> Trip:
    try:
        trip = queries.get_trip(id, user.id)
        return trip
    except TripDoesNotExist:
        raise HTTPException(status_code=404, detail="Trip not found.")
    except TripDatabaseError:
        raise HTTPException(status_code=500, detail="Error retrieving trip.")


# @router.post("/")
# def create_trip(trip: TripRequest, queries: TripQueries = Depends()) -> Trip:
#     try:
#         new_trip = queries.create_trip(trip)
#         return new_trip
#     except TripCreationError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except TripDatabaseError as e:
#         raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
def create_trip(
    trip: TripRequest,
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: TripQueries = Depends(),
) -> Trip:
    try:
        new_trip = queries.create_trip(trip, user.id)
        return new_trip
    except TripCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TripDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
