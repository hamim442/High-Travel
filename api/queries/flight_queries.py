import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from models.flights import Flight, FlightRequest
from utils.exceptions import (
    FlightDatabaseError,
    FlightDoesNotExist,
    FlightCreationError,
    DatabaseURLException,
)


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )


pool = ConnectionPool(database_url)


class FlightQueries:

    def get_all_flights(self) -> list[Flight]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Flight)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM flights;
                        """
                    )
                    flights = result.fetchall()
                    return flights
        except psycopg.Error as e:
            print(f"Error retrieving all flights: {e}")
            raise FlightDatabaseError("Error retrieving all flights")

    def get_flight(self, id: int) -> Flight:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Flight)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM flights
                        WHERE flights.id = %s;
                        """,
                        (id,),
                    )
                    flight = result.fetchone()
                    if flight is None:
                        raise FlightDoesNotExist(f"No flight with id {id}.")
                    return flight
        except psycopg.Error as e:
            print(f"Error retrieving flight with id {id}: {e}")
            raise FlightDatabaseError(
                f"Error retrieving flight with id {id}"
            )

    def create_flight(self, flight: FlightRequest) -> Flight:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Flight)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO flights (
                                flight_number,
                                departure_time,
                                arrival_time,
                                departure_airport,
                                arrival_airport,
                                airline_id,
                                trip_id,
                                price
                            )
                            VALUES (
                                %(flight_number)s,
                                %(departure_time)s,
                                %(arrival_time)s,
                                %(departure_airport)s,
                                %(arrival_airport)s,
                                %(airline_id)s,
                                %(trip_id)s,
                                %(price)s
                            )
                            RETURNING *;
                        """,
                        {
                            "flight_number": flight.flight_number,
                            "departure_time": flight.departure_time,
                            "arrival_time": flight.arrival_time,
                            "departure_airport": flight.departure_airport,
                            "arrival_airport": flight.arrival_airport,
                            "airline_id": flight.airline_id,
                            "trip_id": flight.trip_id,
                            "price": flight.price
                        }
                    )

                    new_flight = result.fetchone()

                    if new_flight is None:
                        raise FlightCreationError("Error creating flight")
                    return new_flight

        except UniqueViolation:
            raise FlightCreationError(
                f"Flight name '{flight.name}' already exists."
            )

        except psycopg.Error as e:
            print(f"Error creating flight: {e}")
            raise FlightDatabaseError("Error creating flight")

    def delete_flight(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM flights
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting flight with id {id}: {e}")
            raise FlightDatabaseError(f"Error deleting flight with id {id}")
