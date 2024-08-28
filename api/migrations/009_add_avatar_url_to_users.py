steps = [
    [
        # "Up" SQL statement to add the column
        """--sql
        ALTER TABLE users
        ADD COLUMN avatar_url TEXT NOT NULL DEFAULT 'http://placehold.co/512x512';
        """,
        # "Down" SQL statement to drop the column
        """--sql
        ALTER TABLE users
        DROP COLUMN avatar_url;
        """,
    ]
]
