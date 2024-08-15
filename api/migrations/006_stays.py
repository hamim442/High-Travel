steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE stays (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL UNIQUE,
            logo_picture_url VARCHAR(300) NOT NULL
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE stays;
        """,
    ],
    [
        """--sql
        INSERT INTO stays (name, logo_picture_url) VALUES
       ('Marriott International', 'https://logo.clearbit.com/marriott.com'),
    ('Hilton Hotels & Resorts', 'https://logo.clearbit.com/hilton.com'),
    ('Hyatt', 'https://logo.clearbit.com/hyatt.com'),
    ('InterContinental Hotels Group (IHG)', 'https://logo.clearbit.com/ihg.com'),
    ('Wyndham Hotels & Resorts', 'https://logo.clearbit.com/wyndhamhotels.com'),
    ('AccorHotels', 'https://logo.clearbit.com/accorhotels.com'),
    ('Radisson Hotel Group', 'https://logo.clearbit.com/radissonhotels.com'),
    ('Best Western Hotels & Resorts', 'https://logo.clearbit.com/bestwestern.com'),
    ('Choice Hotels', 'https://logo.clearbit.com/choicehotels.com'),
    ('Four Seasons Hotels and Resorts', 'https://logo.clearbit.com/fourseasons.com'),
    ('Mandarin Oriental', 'https://logo.clearbit.com/mandarinoriental.com'),
    ('Shangri-La Hotels and Resorts', 'https://logo.clearbit.com/shangri-la.com'),
    ('Fairmont Hotels and Resorts', 'https://logo.clearbit.com/fairmont.com'),
    ('Ritz-Carlton', 'https://logo.clearbit.com/ritzcarlton.com'),
    ('Rosewood Hotels & Resorts', 'https://logo.clearbit.com/rosewoodhotels.com'),
    ('St. Regis Hotels & Resorts', 'https://logo.clearbit.com/stregis.com'),
    ('Aman Resorts', 'https://logo.clearbit.com/aman.com'),
    ('Banyan Tree Hotels & Resorts', 'https://logo.clearbit.com/banyantree.com'),
    ('Six Senses Hotels Resorts Spas', 'https://logo.clearbit.com/sixsenses.com'),
    ('Jumeirah Group', 'https://logo.clearbit.com/jumeirah.com'),
    ('Mövenpick Hotels & Resorts', 'https://logo.clearbit.com/movenpick.com'),
    ('Langham Hospitality Group', 'https://logo.clearbit.com/langhamhotels.com'),
    ('Kempinski Hotels', 'https://logo.clearbit.com/kempinski.com'),
    ('Loews Hotels', 'https://logo.clearbit.com/loewshotels.com'),
    ('Oberoi Hotels & Resorts', 'https://logo.clearbit.com/oberoihotels.com'),
    ('Taj Hotels Resorts and Palaces', 'https://logo.clearbit.com/tajhotels.com'),
    ('LHW (Leading Hotels of the World)', 'https://logo.clearbit.com/lhw.com'),
    ('Soneva', 'https://logo.clearbit.com/soneva.com'),
    ('Alila Hotels and Resorts', 'https://logo.clearbit.com/alilahotels.com'),
    ('Anantara Hotels, Resorts & Spas', 'https://logo.clearbit.com/anantara.com'),
    ('Club Med', 'https://logo.clearbit.com/clubmed.com'),
    ('Relais & Châteaux', 'https://logo.clearbit.com/relaischateaux.com'),
    ('Viceroy Hotels and Resorts', 'https://logo.clearbit.com/viceroyhotelsandresorts.com'),
    ('Airbnb', 'https://logo.clearbit.com/airbnb.com'),
    ('Vrbo', 'https://logo.clearbit.com/vrbo.com'),
    ('Expedia', 'https://logo.clearbit.com/expedia.com'),
    ('Booking.com', 'https://logo.clearbit.com/booking.com'),
    ('Hotels.com', 'https://logo.clearbit.com/hotels.com'),
    ('Trivago', 'https://logo.clearbit.com/trivago.com'),
    ('Kayak', 'https://logo.clearbit.com/kayak.com'),
    ('Orbitz', 'https://logo.clearbit.com/orbitz.com'),
    ('Travelocity', 'https://logo.clearbit.com/travelocity.com'),
    ('Priceline', 'https://logo.clearbit.com/priceline.com'),
    ('Agoda', 'https://logo.clearbit.com/agoda.com'),
    ('TripAdvisor', 'https://logo.clearbit.com/tripadvisor.com'),
    ('Hopper', 'https://logo.clearbit.com/hopper.com'),
    ('OYO Rooms', 'https://logo.clearbit.com/oyorooms.com'),
    ('TUI Group', 'https://logo.clearbit.com/tui.com'),
    ('Ctrip', 'https://logo.clearbit.com/ctrip.com'),
    ('HRS Hotel Reservation Service', 'https://logo.clearbit.com/hrs.com');
        """,
        # "Down" SQL statement
        """--sql
        DELETE FROM stays WHERE id BETWEEN 1 AND 25;
        """,
    ],
]
