import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from models.accommodations import Accommodation, AccommodationRequest
from utils.exceptions import (
    AccommodationDatabaseError,
    AccommodationDoesNotExist,
    AccommodationCreationError,
    DatabaseURLException,
)

database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )

pool = ConnectionPool(database_url)


class AccommodationQueries:

    def get_all_accommodations(self, user_id: int) -> list[Accommodation]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT accommodations.*
                            FROM accommodations
                            JOIN trips ON accommodations.trip_id = trips.id
                            WHERE trips.user_id = %s;
                        """,
                        (user_id,),
                    )
                    accommodations = result.fetchall()
                    return accommodations
        except psycopg.Error as e:
            print(f"Error retrieving accommodations: {e}")
            raise AccommodationDatabaseError(
                "Error retrieving accommodations."
            )

    def get_accommodation(self, id: int, user_id: int) -> Accommodation:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT accommodations.*
                            FROM accommodations
                            JOIN trips ON accommodations.trip_id = trips.id
                            WHERE accommodations.id = %s AND trips.user_id = %s;
                        """,
                        (id, user_id),
                    )
                    accommodation = result.fetchone()
                    if accommodation is None:
                        raise AccommodationDoesNotExist(
                            f"No accommodation with id {id}."
                        )
                    return accommodation
        except psycopg.Error as e:
            print(f"Error retrieving accommodation with id {id}: {e}.")
            raise AccommodationDatabaseError(
                f"Error retrieving accommodation with id {id}."
            )

    def create_accommodation(
        self, accommodation: AccommodationRequest
    ) -> Accommodation:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO accommodations (
                                stays_id, address, city, state_province, zip_code, country,
                                phone, email, check_in_date, check_out_date,
                                number_of_guests, total_price, notes, trip_id
                            )
                            VALUES (
                                %(stays_id)s, %(address)s, %(city)s, %(state_province)s, %(zip_code)s,
                                %(country)s, %(phone)s, %(email)s, %(check_in_date)s, %(check_out_date)s,
                                %(number_of_guests)s, %(total_price)s, %(notes)s, %(trip_id)s
                            )
                            RETURNING *;
                        """,
                        accommodation.model_dump(),
                    )
                    new_accommodation = result.fetchone()
                    if new_accommodation is None:
                        raise AccommodationCreationError(
                            "Error creating accommodation."
                        )
                    return new_accommodation
        except psycopg.Error as e:
            print(f"Error creating accommodation: {e}.")
            raise AccommodationDatabaseError("Error creating accommodation.")
