import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from models.stays import Stay, StayRequest
from utils.exceptions import (
    DatabaseURLException,
    StayCreationError,
    StayDatabaseError,
    StayDoesNotExist,
)


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )


pool = ConnectionPool(database_url)


class StayQueries:

    def get_all_stays(self) -> list[Stay]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Stay)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM stays;
                        """
                    )
                    stays = result.fetchall()
                    return stays
        except psycopg.Error as e:
            print(f'Error retrieving all stays: {e}')
            raise StayDatabaseError

    def get_stay(self, id: int) -> Stay:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Stay)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM stays
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    stay = result.fetchone()
                    if stay is None:
                        raise StayDoesNotExist(f"No stay with id {id}.")
                    return stay
        except psycopg.Error as e:
            print(f"Error retrieving stay with id {id}: {e}.")
            raise StayDatabaseError(f"Error retrieving stay with id {id}.")

    def create_stay(self, stay: StayRequest) -> Stay:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Stay)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO stays (
                                name,
                                logo_picture_url
                            )
                            VALUES (
                                %(name)s,
                                %(logo_picture_url)s
                            )
                            RETURNING *;
                        """,
                        {
                            "name": stay.name,
                            "logo_picture_url": stay.logo_picture_url,
                        },
                    )
                    new_stay = result.fetchone()
                    if new_stay is None:
                        raise StayCreationError("Error creating stay.")
                    return new_stay
        except UniqueViolation:
            raise StayCreationError(
                f"Stay '{stay.name}' already exists."
            )
        except psycopg.Error as e:
            print(f"Error creating stay: {e}.")
            raise StayDatabaseError("Error creating stay.")
