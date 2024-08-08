steps = [
    [
        # "Up" SQL statement
        """--sql
        ALTER TABLE samples
        ADD user_id integer NOT NULL DEFAULT(1) REFERENCES users(id);
        """,
        # "Down" SQL statement
        """--sql
        DROP COLUMN user_id;
        """,
    ],
]
