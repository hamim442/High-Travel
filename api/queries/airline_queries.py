import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from models.airlines import Airline, AirlineRequest
from utils.exceptions import (
    AirlineDatabaseError,
    AirlineDoesNotExist,
    AirlineCreationError,
    DatabaseURLException,
)

database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )

pool = ConnectionPool(database_url)


class AirlineQueries:

    def get_all_airlines(self) -> list[Airline]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Airline)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM airlines;
                        """
                    )
                    airlines = result.fetchall()
                    return airlines
        except psycopg.Error as e:
            print(f"Error retrieving all airlines: {e}")
            raise AirlineDatabaseError("Error retrieving all airlines")

    def get_airline(self, id: int) -> Airline:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Airline)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM airlines
                            WHERE airlines.id = %s;
                        """,
                        (id,),
                    )
                    airline = result.fetchone()
                    if airline is None:
                        raise AirlineDoesNotExist(f"No airline with id {id}.")
                    return airline
        except psycopg.Error as e:
            print(f"Error retrieving airline with id {id}: {e}")
            raise AirlineDatabaseError(
                f"Error retrieving airline with id {id}"
            )

    def create_airline(self, airline: AirlineRequest) -> Airline:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Airline)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO airlines (name, logo_picture_url)
                            VALUES (%(name)s, %(logo_picture_url)s)
                            RETURNING *;
                        """,
                        {
                            "name": airline.name,
                            "logo_picture_url": airline.logo_picture_url,
                        },
                    )

                    new_airline = result.fetchone()

                    if new_airline is None:
                        raise AirlineCreationError("Error creating airline")
                    return new_airline

        except UniqueViolation:
            raise AirlineCreationError(
                f"Airline name '{airline.name}' already exists."
            )

        except psycopg.Error as e:
            print(f"Error creating airline: {e}")
            raise AirlineDatabaseError("Error creating airline")

    def delete_airline(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM airlines
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting airline with id {id}: {e}")
            raise AirlineDatabaseError(f"Error deleting airline with id {id}")
