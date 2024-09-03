import os
import psycopg
from typing import Optional
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from datetime import datetime
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

    def delete_train(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM trains
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting train with id {id}: {e}")
            raise TrainDatabaseError(f"Error deleting train with id {id}")

    def edit_train(
        self,
        train_id: int,
        train_number: Optional[str] = None,
        departure_time: Optional[datetime] = None,
        arrival_time: Optional[datetime] = None,
        departure_station: Optional[str] = None,
        arrival_station: Optional[str] = None,
        trip_id: Optional[int] = None,
        price: Optional[int] = None
    ) -> Train:

        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Train)) as cur:
                    update_fields = []
                    update_values = []

                    if train_number:
                        update_fields.append("train_number = %s")
                        update_values.append(train_number)
                    if departure_time:
                        update_fields.append("departure_time = %s")
                        update_values.append(departure_time)
                    if arrival_time:
                        update_fields.append("arrival_time = %s")
                        update_values.append(arrival_time)
                    if departure_station:
                        update_fields.append("departure_station = %s")
                        update_values.append(departure_station)
                    if arrival_station:
                        update_fields.append("arrival_station = %s")
                        update_values.append(arrival_station)
                    if trip_id:
                        update_fields.append("trip_id = %s")
                        update_values.append(trip_id)
                    if price is not None:
                        update_fields.append("price = %s")
                        update_values.append(price)

                    if not update_fields:
                        raise ValueError("No fields provided for update.")

                    update_values.append(train_id)
                    sql = f"""--sql
                        UPDATE trains
                        SET {', '.join(update_fields)}
                        WHERE id = %s
                        RETURNING *;
                    """
                    cur.execute(
                        sql,
                        update_values,
                    )

                    train = cur.fetchone()
                    if not train:
                        raise TrainDoesNotExist(f"Train with id {train_id} does not exist.")

                    return train

        except psycopg.Error as e:
            print(e)
            raise TrainDatabaseError(f"Could not update train {train_id}")
        except ValueError as e:
            print(e)
            raise TrainDatabaseError("No fields provided for update.")
