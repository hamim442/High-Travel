from fastapi import APIRouter, Depends, HTTPException
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
