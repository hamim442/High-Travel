from fastapi import APIRouter, Depends, HTTPException
from queries.car_queries import (
    CarQueries,
    CarDoesNotExist,
    CarDatabaseError,
    CarCreationError,
)
from models.cars import Car, CarRequest


router = APIRouter(tags=["Car"], prefix="/api/cars")


@router.get("/")
async def get_all_cars(
    queries: CarQueries = Depends(),
) -> list[Car]:
    try:
        cars = queries.get_all_cars()
        return cars
    except CarDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve cars."
        )


@router.get("/{id}")
def get_car(id: int, queries: CarQueries = Depends()) -> Car:
    try:
        car = queries.get_car(id)
        return car
    except CarDoesNotExist:
        raise HTTPException(status_code=404, detail="Car not found")
    except CarDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve car."
        )


@router.post("/")
def create_car(
    car: CarRequest, queries: CarQueries = Depends()
) -> Car:
    try:
        new_car = queries.create_car(car)
        return new_car
    except CarCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except CarDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}")
def delete_car(
    id: int,
    queries: CarQueries = Depends(),
) -> dict:
    try:
        success = queries.delete_car(id)
        if not success:
            raise CarDoesNotExist(f"Car with id {id} does not exist.")
        return {"status": "Car deleted successfully."}
    except CarDoesNotExist:
        raise HTTPException(status_code=404, detail="Car not found.")
    except CarDatabaseError:
        raise HTTPException(status_code=500, detail="Error deleting car.")
