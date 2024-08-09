steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE flights (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description TEXT NULL,
            departure_time DATETIME NOT NULL,
            arrival_time DATETIME NOT NULL,
            departure_airport VARCHAR(100) NOT NULL,
            arrival_airport VARCHAR(100) NOT NULL,
            flight_number INTEGER NULL,
            airline_id INTEGER NULL REFERENCES airlines (id),
            trip_id INTEGER NOT NULL REFERENCES trip (id),
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE flights;
        """,
    ],
]
