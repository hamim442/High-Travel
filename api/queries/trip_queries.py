import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from models.trips import Trip, TripRequest
from utils.exceptions import (
    TripDatabaseError,
    TripDoesNotExist,
    TripCreationError,
    DatabaseURLException,
)


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )


pool = ConnectionPool(database_url)


class TripQueries:

    def get_user_trips(self, user_id: int) -> list[Trip]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Trip)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM trips
                            WHERE user_id = %s;
                        """,
                        (user_id,),
                    )
                    trips = result.fetchall()
                    return trips
        except psycopg.Error as e:
            print(f"Error retrieving trips for user {user_id}: {e}.")
            raise TripDatabaseError(
                f"Error retrieving trips for user {user_id}."
            )

    def get_trip(self, id: int, user_id: int) -> Trip:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Trip)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM trips
                            WHERE id = %s AND user_id = %s;
                        """,
                        (id, user_id),
                    )
                    trip = result.fetchone()
                    if trip is None:
                        raise TripDoesNotExist(
                            f"No trip with id {id} for user {user_id}."
                        )
                    return trip
        except psycopg.Error as e:
            print(
                f"Error retrieving trip with id {id} for user {user_id}: {e}."
            )
            raise TripDatabaseError(
                f"Error retrieving trip with id {id} for user {user_id}."
            )

    def create_trip(self, trip: TripRequest, user_id: int) -> Trip:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Trip)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO trips (
                                city_id,
                                start_date,
                                end_date,
                                user_id
                            )
                            VALUES (
                                %(city_id)s,
                                %(start_date)s,
                                %(end_date)s,
                                %(user_id)s
                            )
                            RETURNING *;
                        """,
                        {
                            "city_id": trip.city_id,
                            "start_date": trip.start_date,
                            "end_date": trip.end_date,
                            "user_id": user_id,
                        },
                    )
                    new_trip = result.fetchone()
                    if new_trip is None:
                        raise TripCreationError("Error creating trip.")
                    return new_trip
        except psycopg.Error as e:
            print(f"Error creating trip for user {user_id}: {e}.")
            raise TripDatabaseError("Error creating trip.")

    def delete_trip(self, id: int, user_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM trips
                            WHERE id = %s AND user_id = %s;
                        """,
                        (id, user_id),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting trip with id {id} for user {user_id}: {e}.")
            raise TripDatabaseError(
                f"Error deleting trip with id {id} for user {user_id}."
            )
