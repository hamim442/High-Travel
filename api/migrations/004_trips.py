steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE trips (
            id SERIAL PRIMARY KEY NOT NULL,
            city_id INTEGER NULL REFERENCES cities (id),
            start_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE trips;
        """,
    ],
]
