steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE trains (
            id SERIAL PRIMARY KEY NOT NULL,
            train_number VARCHAR(50) NOT NULL,
            departure_time TIMESTAMP NOT NULL,
            arrival_time TIMESTAMP NOT NULL,
            departure_station VARCHAR(100) NOT NULL,
            arrival_station VARCHAR(100) NOT NULL,
            price INTEGER NOT NULL,
            trip_id INTEGER NOT NULL REFERENCES trips (id)
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE trains;
        """,
    ],
]
