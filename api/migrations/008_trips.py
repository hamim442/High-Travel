steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE trips (
            id SERIAL PRIMARY KEY NOT NULL,
            city_id INTEGER NULL REFERENCES cities (id),
            start_date DATETIME NOT NULL,
            end_date DATETIME NOT NULL,
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE trips;
        """,
    ],
]
