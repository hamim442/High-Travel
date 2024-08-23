import random
import time
from fastapi import APIRouter, Depends, HTTPException
from queries.city_queries import (
    CityQueries,
    CityDoesNotExist,
    CityDatabaseError,
    CityCreationError,
)
from models.cities import City, CityRequest


router = APIRouter(tags=["City"], prefix="/api/cities")


cached_cities = []
cache_time = 0
CACHE_DURATION = 86400  # 24 hours in secs


@router.get("/random")
def get_random_cities(queries: CityQueries = Depends()) -> list[City]:
    global cached_cities, cache_time
    current_time = time.time()

    if current_time - cache_time > CACHE_DURATION or not cached_cities:
        all_cities = queries.get_all_cities()
        if len(all_cities) >= 5:
            cached_cities = random.sample(all_cities, 5)
        else:
            cached_cities = all_cities
        cache_time = current_time

    return cached_cities


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
