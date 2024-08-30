import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from models.trains import Train, TrainRequest
from utils.exceptions import (
    TrainDatabaseError,
    TrainDoesNotExist,
    TrainCreationError,
    DatabaseURLException,
)

database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )

pool = ConnectionPool(database_url)


class TrainQueries:

    def get_all_trains(self) -> list[Train]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Train)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM trains;
                        """
                    )
                    trains = result.fetchall()
                    return trains
        except psycopg.Error as e:
            print(f"Error retrieving all trains: {e}")
            raise TrainDatabaseError("Error retrieving all trains")

    def get_train(self, id: int) -> Train:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Train)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM trains
                        WHERE trains.id = %s;
                        """,
                        (id,),
                    )
                    train = result.fetchone()
                    if train is None:
                        raise TrainDoesNotExist(f"No train with id {id}.")
                    return train
        except psycopg.Error as e:
            print(f"Error retrieving train with id {id}: {e}")
            raise TrainDatabaseError(
                f"Error retrieving train with id {id}"
            )

    def create_train(self, train: TrainRequest) -> Train:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Train)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO trains (
                                train_number,
                                departure_time,
                                arrival_time,
                                departure_station,
                                arrival_station,
                                trip_id,
                                price  -- Added the price field
                            )
                            VALUES (
                                %(train_number)s,
                                %(departure_time)s,
                                %(arrival_time)s,
                                %(departure_station)s,
                                %(arrival_station)s,
                                %(trip_id)s,
                                %(price)s  -- Added the price value
                            )
                            RETURNING *;
                        """,
                        {
                            "train_number": train.train_number,
                            "departure_time": train.departure_time,
                            "arrival_time": train.arrival_time,
                            "departure_station": train.departure_station,
                            "arrival_station": train.arrival_station,
                            "trip_id": train.trip_id,
                            "price": train.price
                        }
                    )

                    new_train = result.fetchone()

                    if new_train is None:
                        raise TrainCreationError("Error creating train")
                    return new_train

        except UniqueViolation:
            raise TrainCreationError(
                f"Train number '{train.train_number}' already exists."
            )

        except psycopg.Error as e:
            print(f"Error creating train: {e}")
            raise TrainDatabaseError("Error creating train")
