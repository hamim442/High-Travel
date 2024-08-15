from fastapi import APIRouter, Depends, HTTPException
from queries.user_trip_queries import UserTripQueries, UserTripDatabaseError
from models.user_trip import UserTripRequest, UserTripResponse

router = APIRouter(tags=["UserTrip"], prefix="/api/user-trip")


@router.post("/")
def add_contributor(
    user_trip: UserTripRequest, queries: UserTripQueries = Depends()
) -> UserTripResponse:
    try:
        new_user_trip = queries.add_contributor(user_trip)
        return new_user_trip
    except UserTripDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{trip_id}")
def get_contributors(
    trip_id: int, queries: UserTripQueries = Depends()
) -> list[UserTripResponse]:
    try:
        contributors = queries.get_contributors_for_trip(trip_id)
        return contributors
    except UserTripDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/")
def remove_contributor(
    user_id: int, trip_id: int, queries: UserTripQueries = Depends()
) -> None:
    try:
        queries.remove_contributor(user_id, trip_id)
    except UserTripDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
