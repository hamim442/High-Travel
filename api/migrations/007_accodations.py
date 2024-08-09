steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE accommodations (
            id SERIAL PRIMARY KEY NOT NULL,
            stays_id INTEGER NULL REFERENCES stays (id),
            address VARCHAR(500) NOT NULL,
            city VARCHAR(100) NOT NULL,
            state_province VARCHAR(100) NULL,
            zip_code VARCHAR(100) NOT NULL,
            country VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NULL,
            email VARCHAR(300) NULL,
            check_in_date DATETIME NOT NULL,
            check_out_date DATETIME NOT NULL,
            number_of_guests INTEGER NOT NULL,
            total_price DECIMAL NOT NULL,
            notes TEXT NULL,
            trip_id INTEGER NOT NULL REFERENCES trip (id),
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE accommodations;
        """,
    ],
]
