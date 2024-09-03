steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE flights (
            id SERIAL PRIMARY KEY NOT NULL,
            flight_number VARCHAR(20) NULL,
            departure_time TIMESTAMP NOT NULL,
            arrival_time TIMESTAMP NOT NULL,
            departure_airport VARCHAR(100) NOT NULL,
            arrival_airport VARCHAR(100) NOT NULL,
            price INTEGER NOT NULL,
            airline_id INTEGER NULL REFERENCES airlines (id),
            trip_id INTEGER NOT NULL REFERENCES trips (id)
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE flights;
        """,
    ],
]
