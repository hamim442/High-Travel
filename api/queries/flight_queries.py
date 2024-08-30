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
                                name,
                                description,
                                departure_time,
                                arrival_time,
                                departure_airport,
                                arrival_airport,
                                flight_number,
                                airline_id,
                                trip_id,
                                price  -- Added the price field
                            )
                            VALUES (
                                %(name)s,
                                %(description)s,
                                %(departure_time)s,
                                %(arrival_time)s,
                                %(departure_airport)s,
                                %(arrival_airport)s,
                                %(flight_number)s,
                                %(airline_id)s,
                                %(trip_id)s,
                                %(price)s  -- Added the price value
                            )
                            RETURNING *;
                        """,
                        {
                            "name": flight.name,
                            "description": flight.description,
                            "departure_time": flight.departure_time,
                            "arrival_time": flight.arrival_time,
                            "departure_airport": flight.departure_airport,
                            "arrival_airport": flight.arrival_airport,
                            "flight_number": flight.flight_number,
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
