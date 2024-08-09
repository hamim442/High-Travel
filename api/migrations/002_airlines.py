steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE airlines (
            id serial primary key not null,
            name varchar(100) not null,
            logo_picture_url varchar(300) not null
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE airlines;
        """,
    ],
    [
        """--sql
        INSERT INTO airlines (name, logo_picture_url)
     VALUES
    ('American Airlines', 'https://logo.clearbit.com/americanairlines.com'),
    ('Delta Air Lines', 'https://logo.clearbit.com/delta.com'),
    ('United Airlines', 'https://logo.clearbit.com/united.com'),
    ('Emirates', 'https://logo.clearbit.com/emirates.com'),
    ('Lufthansa', 'https://logo.clearbit.com/lufthansa.com'),
    ('Air France', 'https://logo.clearbit.com/airfrance.com'),
    ('British Airways', 'https://logo.clearbit.com/britishairways.com'),
    ('Southwest Airlines', 'https://logo.clearbit.com/southwest.com'),
    ('China Southern Airlines', 'https://logo.clearbit.com/chinasouthern.com'),
    ('Qatar Airways', 'https://logo.clearbit.com/qatarairways.com'),
    ('Cathay Pacific', 'https://logo.clearbit.com/cathaypacific.com'),
    ('Singapore Airlines', 'https://logo.clearbit.com/singaporeair.com'),
    ('Qantas', 'https://logo.clearbit.com/qantas.com'),
    ('Turkish Airlines', 'https://logo.clearbit.com/turkishairlines.com'),
    ('KLM', 'https://logo.clearbit.com/klm.com'),
    ('ANA (All Nippon Airways)', 'https://logo.clearbit.com/ana.co.jp'),
    ('Japan Airlines', 'https://logo.clearbit.com/jal.co.jp'),
    ('Air Canada', 'https://logo.clearbit.com/aircanada.com'),
    ('Etihad Airways', 'https://logo.clearbit.com/etihad.com'),
    ('EVA Air', 'https://logo.clearbit.com/evaair.com'),
    ('Swiss International Air Lines', 'https://logo.clearbit.com/swiss.com'),
    ('Thai Airways', 'https://logo.clearbit.com/thaiairways.com'),
    ('Korean Air', 'https://logo.clearbit.com/koreanair.com'),
    ('Iberia', 'https://logo.clearbit.com/iberia.com'),
    ('Finnair', 'https://logo.clearbit.com/finnair.com');
    """,
    # "Down" SQL statement to delete all airlines

    """--sql
    DELETE FROM airlines WHERE name IN (
        'American Airlines', 'Delta Air Lines', 'United Airlines', 'Emirates',
        'Lufthansa', 'Air France', 'British Airways', 'Southwest Airlines',
        'China Southern Airlines', 'Qatar Airways', 'Cathay Pacific', 'Singapore Airlines',
        'Qantas', 'Turkish Airlines', 'KLM', 'ANA (All Nippon Airways)',
        'Japan Airlines', 'Air Canada', 'Etihad Airways', 'EVA Air',
        'Swiss International Air Lines', 'Thai Airways', 'Korean Air',
        'Iberia', 'Finnair'
    );
    """,
        """--sql
        DROP TABLE airlines;
        """,
    ]
]
