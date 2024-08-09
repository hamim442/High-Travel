steps = [
    [
        """"--sql
        CREATE TABLE users_trips (
            user_id INTEGER NOT NULL REFERENCES users (id),
            trip_id INTEGER NOT NULL REFERENCES trips (id)

        )
        """,
        """
        DROP TABLE users_trips
        """
    ]
]
