steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE accommodations (
            id SERIAL PRIMARY KEY NOT NULL,
            stays_id INTEGER NULL REFERENCES stays (id),
            address VARCHAR(255) NOT NULL,
            city VARCHAR(100) NOT NULL,
            state_province VARCHAR(100) NULL,
            zip_code VARCHAR(20) NOT NULL,
            country VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NULL,
            email VARCHAR(255) NULL,
            check_in_date TIMESTAMP NOT NULL,
            check_out_date TIMESTAMP NOT NULL,
            number_of_guests INTEGER NOT NULL,
            total_price DECIMAL(10, 2) NOT NULL,
            notes TEXT NULL,
            trip_id INTEGER NOT NULL REFERENCES trips (id) ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE accommodations;
        """,
    ],
]
