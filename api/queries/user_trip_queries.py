import os
import psycopg
from psycopg_pool import ConnectionPool
from psycopg.rows import class_row
from models.user_trip import (
    UserTripRequest,
    UserTripResponse,
    TripByUserResponse,
)
from utils.exceptions import (
    UserTripDatabaseError,
    UserTripCreationError,
    DatabaseURLException,
)

database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )

pool = ConnectionPool(database_url)


class UserTripQueries:

    def add_contributor(self, user_trip: UserTripRequest) -> UserTripResponse:
        try:
            with pool.connection() as conn:
                with conn.cursor(
                    row_factory=class_row(UserTripResponse)
                ) as cur:
                    result = cur.execute(
                        """--sql
                        INSERT INTO users_trips (user_id, trip_id)
                        VALUES (%(user_id)s, %(trip_id)s)
                        RETURNING *;
                        """,
                        {
                            "user_id": user_trip.user_id,
                            "trip_id": user_trip.trip_id,
                        },
                    )
                    new_user_trip = result.fetchone()
                    if new_user_trip is None:
                        raise UserTripCreationError(
                            "Error adding contributor."
                        )
                    return new_user_trip
        except psycopg.Error as e:
            print(f"Error adding contributor: {e}.")
            raise UserTripDatabaseError("Error adding contributor.")

    def get_contributors_for_trip(
        self, trip_id: int
    ) -> list[UserTripResponse]:
        try:
            with pool.connection() as conn:
                with conn.cursor(
                    row_factory=class_row(UserTripResponse)
                ) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT * FROM users_trips WHERE trip_id = %s;
                        """,
                        (trip_id,),
                    )
                    contributors = result.fetchall()
                    return contributors
        except psycopg.Error as e:
            print(f"Error retrieving contributors: {e}.")
            raise UserTripDatabaseError("Error retrieving contributors.")

    def remove_contributor(self, user_id: int, trip_id: int) -> None:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                        DELETE FROM users_trips WHERE user_id = %s AND trip_id = %s;
                        """,
                        (user_id, trip_id),
                    )
        except psycopg.Error as e:
            print(f"Error removing contributor: {e}.")
            raise UserTripDatabaseError("Error removing contributor.")

    # def get_trips_by_userid(self, trip_id: int,
    #                         start_date: str,
    #                         end_date: str,
    #                         city_name: str,
    #                         city_picture_url: str,
    #                         country_name: str) -> list[TripByUserResponse]:
    #     try:
    #         with pool.connection() as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute
    #                     """--sql
    #                     SELECT * FROM user_id WHERE
    #                     """
