from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from datetime import datetime
from queries.train_queries import (
    TrainQueries,
    TrainDoesNotExist,
    TrainDatabaseError,
    TrainCreationError,
)
from models.trains import Train, TrainRequest


router = APIRouter(tags=["Train"], prefix="/api/trains")


@router.get("/")
async def get_all_trains(
    queries: TrainQueries = Depends(),
) -> list[Train]:
    try:
        trains = queries.get_all_trains()
        return trains
    except TrainDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve trains."
        )


@router.get("/{id}")
def get_train(id: int, queries: TrainQueries = Depends()) -> Train:
    try:
        train = queries.get_train(id)
        return train
    except TrainDoesNotExist:
        raise HTTPException(status_code=404, detail="Train not found")
    except TrainDatabaseError:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve train."
        )


@router.post("/")
def create_train(
    train: TrainRequest, queries: TrainQueries = Depends()
) -> Train:
    try:
        new_train = queries.create_train(train)
        return new_train
    except TrainCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TrainDatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}")
def delete_train(
    id: int,
    queries: TrainQueries = Depends(),
) -> dict:
    try:
        success = queries.delete_train(id)
        if not success:
            raise TrainDoesNotExist(f"Train with id {id} does not exist.")
        return {"status": "Train deleted successfully."}
    except TrainDoesNotExist:
        raise HTTPException(status_code=404, detail="Train not found.")
    except TrainDatabaseError:
        raise HTTPException(status_code=500, detail="Error deleting train.")


@router.put("/{id}")
def update_train(
    id: int,
    train_number: Optional[str] = None,
    departure_time: Optional[datetime] = None,
    arrival_time: Optional[datetime] = None,
    departure_station: Optional[str] = None,
    arrival_station: Optional[str] = None,
    trip_id: Optional[int] = None,
    price: Optional[int] = None,
    queries: TrainQueries = Depends()
) -> Train:
    try:
        updated_train = queries.edit_train(
            train_id=id,
            train_number=train_number,
            departure_time=departure_time,
            arrival_time=arrival_time,
            departure_station=departure_station,
            arrival_station=arrival_station,
            trip_id=trip_id,
            price=price
        )
        return updated_train
    except TrainDoesNotExist:
        raise HTTPException(status_code=404, detail="Train not found.")
    except TrainDatabaseError:
        raise HTTPException(status_code=500, detail="Error updating train.")
