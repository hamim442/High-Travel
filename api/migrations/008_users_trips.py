steps = [
    [
        """--sql
        CREATE TABLE users_trips (
            user_id INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
            trip_id INTEGER NOT NULL REFERENCES trips (id) ON DELETE CASCADE,
            PRIMARY KEY (user_id, trip_id)
        );
        """,
        """--sql
        DROP TABLE users_trips;
        """,
    ],
]
