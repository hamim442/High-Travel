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

#Allows everyone to see create trips. Make it only authorized user can see it. 
database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )


pool = ConnectionPool(database_url)


class TripQueries:

    def get_all_trips(self) -> list[Trip]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Trip)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM trips;
                        """
                    )
                    trips = result.fetchall()
                    return trips
        except psycopg.Error as e:
            print(f"Error retrieving all trips: {e}.")
            raise TripDatabaseError("Error retrieving all trips.")

    def get_trip(self, id: int) -> Trip:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Trip)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM trips
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    trip = result.fetchone()
                    if trip is None:
                        raise TripDoesNotExist(f"No trip with id {id}.")
                    return trip
        except psycopg.Error as e:
            print(f"Error retrieving trip with id {id}: {e}.")
            raise TripDatabaseError(f"Error retrieving trip with id {id}.")

    def create_trip(self, trip: TripRequest) -> Trip:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Trip)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO trips (city_id, start_date, end_date)
                            VALUES (%(city_id)s, %(start_date)s, %(end_date)s)
                            RETURNING *;
                        """,
                        {
                            "city_id": trip.city_id,
                            "start_date": trip.start_date,
                            "end_date": trip.end_date,
                        },
                    )
                    new_trip = result.fetchone()
                    if new_trip is None:
                        raise TripCreationError("Error creating trip.")
                    return new_trip
        except psycopg.Error as e:
            print(f"Error creating trip: {e}.")
            raise TripDatabaseError("Error creating trip.")
