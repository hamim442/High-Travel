import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from models.cities import City, CityRequest
from utils.exceptions import (
    DatabaseURLException,
    CityDatabaseError,
    CityCreationError,
    CityDoesNotExist,
)


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )


pool = ConnectionPool(database_url)


class CityQueries:

    def get_all_cities(self) -> list[City]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(City)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM cities;
                        """
                    )
                    cities = result.fetchall()
                    return cities
        except psycopg.Error as e:
            print(f"Error retrieving all cities: {e}")
            raise CityDatabaseError("Error retrieving all cities.")

    def get_city(self, id: int) -> City:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(City)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT *
                            FROM cities
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    city = result.fetchone()
                    if city is None:
                        raise CityDoesNotExist(f"No city with id {id}.")
                    return city
        except psycopg.Error as e:
            print(f"Error retrieving city with id {id}: {e}.")
            raise CityDatabaseError(f"Error retrieving city with id {id}.")

    def create_city(self, city: CityRequest) -> City:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(City)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO cities (
                                name,
                                administrative_division,
                                country,
                                picture_url
                            )
                            VALUES (
                                %(name)s,
                                %(administrative_division)s,
                                %(country)s,
                                %(picture_url)s
                            )
                            RETURNING *;
                        """,
                        {
                            "name": city.name,
                            "administrative_division": city.administrative_division,
                            "country": city.country,
                            "picture_url": city.picture_url,
                        },
                    )
                    new_city = result.fetchone()
                    if new_city is None:
                        raise CityCreationError("Error creating city.")
                    return new_city
        except UniqueViolation:
            raise CityCreationError(
                f"City '{city.name}' already exists in '{city.country}'."
            )
        except psycopg.Error as e:
            print(f"Error creating city: {e}.")
            raise CityDatabaseError("Error creating city.")
