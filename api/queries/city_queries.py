import os
import psycopg
from typing import Optional
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
                            SELECT id, name, administrative_division, country, picture_url, description
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
                            SELECT id, name, administrative_division, country, picture_url, description
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

    def search_cities(self, search: str) -> list[City]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(City)) as cur:
                    cur.execute(
                        """--sql
                        SELECT id, name, administrative_division, country, picture_url, description
                        FROM cities
                        WHERE name ILIKE %s
                        LIMIT 10;
                        """,
                        (f"%{search}%",),
                    )
                    return cur.fetchall()
        except psycopg.Error as e:
            print(f"Error searching cities: {e}")
            raise CityDatabaseError("Error searching cities.")

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
                                picture_url,
                                description
                            )
                            VALUES (
                                %(name)s,
                                %(administrative_division)s,
                                %(country)s,
                                %(picture_url)s,
                                %(description)s
                            )
                            RETURNING *;
                        """,
                        {
                            "name": city.name,
                            "administrative_division": city.administrative_division,
                            "country": city.country,
                            "picture_url": city.picture_url,
                            "description": city.description,
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

    def delete_city(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM cities
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting city with id {id}: {e}.")
            raise CityDatabaseError(f"Error deleting city with id {id}.")

    def edit_city(
        self,
        id: int,
        name: Optional[str] = None,
        administrative_division: Optional[str] = None,
        country: Optional[str] = None,
        picture_url: Optional[str] = None,
        description: Optional[str] = None,
    ) -> City:

        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(City)) as cur:
                    update_fields = []
                    update_values = []

                    if name:
                        update_fields.append("name = %s")
                        update_values.append(name)
                    if administrative_division:
                        update_fields.append("administrative_division = %s")
                        update_values.append(administrative_division)
                    if country:
                        update_fields.append("country = %s")
                        update_values.append(country)
                    if picture_url:
                        update_fields.append("picture_url = %s")
                        update_values.append(picture_url)
                    if description:
                        update_fields.append("description = %s")
                        update_values.append(description)

                    update_values.append(id)
                    sql = f"""--sql
                        UPDATE cities
                        SET {', '.join(update_fields)}
                        WHERE id = %s
                        RETURNING *;
                    """
                    cur.execute(
                        sql,
                        update_values,
                    )

                    city = cur.fetchone()
                    if not city:
                        raise CityDoesNotExist(f"{id}")

                    return city

        except psycopg.Error as e:
            print(e)
            raise CityDatabaseError(f"could not update {id}")
        except ValueError as e:
            print(e)
            raise CityDatabaseError("No fields for city update")
