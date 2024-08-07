steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(256) NOT NULL
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE users;
        """,
    ],
]
