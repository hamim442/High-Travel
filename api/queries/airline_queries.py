import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from models.airlines import Airline, AirlineRequest

# from utils.exceptions import (
#     AirlineDatabaseError,
#     AirlineDoesNotExist,
#     AirlineCreationError,
# )

database_url = os.environ.get("DATABASE_URL")

# from superhero app
if database_url is None:
    pass


pool = ConnectionPool(database_url)


class AirlineQueries:
    def get_all_airlines(self) -> list[Airline]:
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
                        pass
                        # raise AirlineDoesNotExist(f"No airline with id {id}.")
                    return airline
        except psycopg.Error as e:
            print(e)
            # raise AirlineDatabaseError(e)

    def create_airline(self, airline):
        pass
