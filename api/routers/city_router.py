from fastapi import APIRouter, Depends, HTTPException
from queries.city_queries import (
    CityQueries,
    CityDoesNotExist,
    CityDatabaseError,
    CityCreationError,
)
from models.cities import City, CityRequest


router = APIRouter(tags=["City"], prefix="/api/cities")


@router.get("/")
def search_cities(
    search: str = "", queries: CityQueries = Depends()
) -> list[City]:
    try:
        if search:
            cities = queries.search_cities(search)
        else:
            cities = queries.get_all_cities()
        return cities
    except CityDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve cities."
        )


@router.get("/")
async def get_all_cities(
    queries: CityQueries = Depends(),
) -> list[City]:
    try:
        cities = queries.get_all_cities()
        return cities
    except CityDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve cities."
        )


@router.get("/{id}")
def get_city(id: int, queries: CityQueries = Depends()) -> City:
    try:
        city = queries.get_city(id)
        return city
    except CityDoesNotExist:
        raise HTTPException(status_code=404, detail="City not found.")
    except CityDatabaseError:
        raise HTTPException(status_code=500, detail="Error retrieving city.")


@router.post("/")
def create_city(city: CityRequest, queries: CityQueries = Depends()) -> City:
    try:
        new_city = queries.create_city(city)
        return new_city
    except CityCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except CityDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}")
def delete_city(id: int, queries: CityQueries = Depends()) -> dict:
    try:
        success = queries.delete_city(id)
        if not success:
            raise CityDoesNotExist(f"City with id {id} does not exist.")
        return {"status": "City deleted successfully."}
    except CityDoesNotExist:
        raise HTTPException(status_code=404, detail="City not found.")
    except CityDatabaseError:
        raise HTTPException(status_code=500, detail="Error deleting city.")
