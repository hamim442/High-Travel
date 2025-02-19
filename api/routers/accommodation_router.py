from fastapi import APIRouter, Depends, HTTPException
from queries.accommodation_queries import (
    AccommodationQueries,
    AccommodationDoesNotExist,
    AccommodationDatabaseError,
    AccommodationCreationError,
)
from models.accommodations import (
    Accommodation,
    AccommodationRequest,
    AccommodationUpdate,
)
from utils.authentication import try_get_jwt_user_data
from models.jwt import JWTUserData


router = APIRouter(tags=["Accommodation"], prefix="/api/accommodations")


@router.get("/")
async def get_all_accommodations(
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: AccommodationQueries = Depends(),
) -> list[Accommodation]:
    try:
        accommodations = queries.get_all_accommodations(user.id)
        return accommodations
    except AccommodationDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve accommodations."
        )


@router.get("/{id}")
def get_accommodation(
    id: int,
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: AccommodationQueries = Depends(),
) -> Accommodation:
    try:
        accommodation = queries.get_accommodation(id, user.id)
        return accommodation
    except AccommodationDoesNotExist:
        raise HTTPException(status_code=404, detail="Accommodation not found.")
    except AccommodationDatabaseError:
        raise HTTPException(
            status_code=500, detail="Error retrieving accommodation."
        )


@router.post("/")
def create_accommodation(
    accommodation: AccommodationRequest,
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: AccommodationQueries = Depends(),
) -> Accommodation:
    try:
        new_accommodation = queries.create_accommodation(accommodation)
        return new_accommodation
    except AccommodationCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except AccommodationDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}")
def delete_accommodation(
    id: int,
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: AccommodationQueries = Depends(),
) -> dict:
    try:
        success = queries.delete_accommodation(id, user.id)
        if not success:
            raise AccommodationDoesNotExist(
                f"Accommodation with id {id} does not exist."
            )
        return {"status": "Accommodation deleted successfully."}
    except AccommodationDoesNotExist:
        raise HTTPException(status_code=404, detail="Accommodation not found.")
    except AccommodationDatabaseError:
        raise HTTPException(
            status_code=500, detail="Error deleting accommodation."
        )


@router.put("/accommodations/{id}")
def edit_accommodation(
    id: int,
    accommdation_update: AccommodationUpdate,
    user: JWTUserData = Depends(try_get_jwt_user_data),
    queries: AccommodationQueries = Depends(),
) -> Accommodation:

    try:
        updated_accommodation = queries.update_accommodation(
            id, user.id, accommdation_update
        )
        return updated_accommodation
    except AccommodationDoesNotExist:
        raise HTTPException(status_code=404, detail="Accommodation not found.")

    except AccommodationDatabaseError:
        raise HTTPException(
            status_code=500, detail="Error updating accommodation."
        )
