import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from psycopg.errors import UniqueViolation
from models.cars import Car, CarRequest
from utils.exceptions import (
    CarDatabaseError,
    CarDoesNotExist,
    CarCreationError,
    DatabaseURLException,
)


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )


pool = ConnectionPool(database_url)


class CarQueries:

    def get_all_cars(self) -> list[Car]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Car)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM cars;
                        """
                    )
                    cars = result.fetchall()
                    return cars
        except psycopg.Error as e:
            print(f"Error retrieving all cars: {e}")
            raise CarDatabaseError("Error retrieving all cars")

    def get_car(self, id: int) -> Car:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Car)) as cur:
                    result = cur.execute(
                        """--sql
                        SELECT *
                        FROM cars
                        WHERE cars.id = %s;
                        """,
                        (id,),
                    )
                    car = result.fetchone()
                    if car is None:
                        raise CarDoesNotExist(f"No car with id {id}.")
                    return car
        except psycopg.Error as e:
            print(f"Error retrieving car with id {id}: {e}")
            raise CarDatabaseError(
                f"Error retrieving car with id {id}"
            )

    def create_car(self, car: CarRequest) -> Car:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Car)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO cars (
                                car_model,
                                rental_company,
                                pickup_time,
                                dropoff_time,
                                pickup_location,
                                dropoff_location,
                                trip_id,
                                price
                            )
                            VALUES (
                                %(car_model)s,
                                %(rental_company)s,
                                %(pickup_time)s,
                                %(dropoff_time)s,
                                %(pickup_location)s,
                                %(dropoff_location)s,
                                %(trip_id)s,
                                %(price)s
                            )
                            RETURNING *;
                        """,
                        {
                            "car_model": car.car_model,
                            "rental_company": car.rental_company,
                            "pickup_time": car.pickup_time,
                            "dropoff_time": car.dropoff_time,
                            "pickup_location": car.pickup_location,
                            "dropoff_location": car.dropoff_location,
                            "trip_id": car.trip_id,
                            "price": car.price,
                        }
                    )

                    new_car = result.fetchone()

                    if new_car is None:
                        raise CarCreationError("Error creating car")
                    return new_car

        except UniqueViolation:
            raise CarCreationError(
                f"Car model '{car.car_model}' with these details already exists."
            )

        except psycopg.Error as e:
            print(f"Error creating car: {e}")
            raise CarDatabaseError("Error creating car")

    def delete_car(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM cars
                            WHERE id = %s;
                        """,
                        (id,),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting car with id {id}: {e}")
            raise CarDatabaseError(f"Error deleting car with id {id}")
