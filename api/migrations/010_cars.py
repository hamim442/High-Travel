steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE cars (
            id SERIAL PRIMARY KEY NOT NULL,
            car_model VARCHAR(100) NOT NULL,
            rental_company VARCHAR(100) NOT NULL,
            pickup_time TIMESTAMP NOT NULL,
            dropoff_time TIMESTAMP NOT NULL,
            pickup_location VARCHAR(150) NOT NULL,
            dropoff_location VARCHAR(150) NOT NULL,
            price INTEGER NOT NULL,
            trip_id INTEGER NOT NULL REFERENCES trips (id)
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE cars;
        """,
    ],
]
