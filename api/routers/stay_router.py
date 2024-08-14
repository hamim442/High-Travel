from fastapi import APIRouter, Depends, HTTPException
from queries.stay_queries import (
    StayQueries,
    StayDoesNotExist,
    StayDatabaseError,
    StayCreationError,
)
from models.stays import Stay, StayRequest


router = APIRouter(tags=["Stay"], prefix="/api/stays")


@router.get("/")
async def get_all_stays(
    queries: StayQueries = Depends(),
) -> list[Stay]:
    try:
        stays = queries.get_all_stays()
        return stays
    except StayDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve stays."
        )


@router.get("/{id}")
def get_stay(id: int, queries: StayQueries = Depends()) -> Stay:
    try:
        stay = queries.get_stay(id)
        return stay
    except StayDoesNotExist:
        raise HTTPException(status_code=404, detail="stay not found.")
    except StayDatabaseError:
        raise HTTPException(status_code=500, detail="Error retrieving stay.")


@router.post("/")
def create_stay(stay: StayRequest, queries: StayQueries = Depends()) -> Stay:
    try:
        new_stay = queries.create_stay(stay)
        return new_stay
    except StayCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except StayDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}")
def delete_stay(
    id: int,
    queries: StayQueries = Depends(),
) -> dict:
    try:
        success = queries.delete_stay(id)
        if not success:
            raise StayDoesNotExist(f"Stay with id {id} does not exist.")
        return {"status": "Stay deleted successfully."}
    except StayDoesNotExist:
        raise HTTPException(status_code=404, detail="Stay not found.")
    except StayDatabaseError:
        raise HTTPException(status_code=500, detail="Error deleting stay.")
