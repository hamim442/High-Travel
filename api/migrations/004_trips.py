steps = [
    [
        # "Up" SQL statement
        """--sql
            CREATE TABLE trips (
                id SERIAL PRIMARY KEY NOT NULL,
                city_id INTEGER NULL REFERENCES cities (id),
                start_date TIMESTAMP NOT NULL,
                end_date TIMESTAMP NOT NULL,
                user_id INTEGER NOT NULL REFERENCES users (id)
            );
        """,
        # "Down" SQL statement
        """--sql
            DROP TABLE trips;
        """,
    ],
]
