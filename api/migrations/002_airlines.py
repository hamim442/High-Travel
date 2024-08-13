steps = [
    [
        # "Up" SQL statement
        """--sql
            CREATE TABLE airlines (
                id serial primary key not null,
                name varchar(100) not null UNIQUE,
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
            ('Southwest Airlines', 'https://logo.clearbit.com/southwest.com'),
            ('China Southern Airlines', 'https://logo.clearbit.com/csair.com'),
            ('Lufthansa', 'https://logo.clearbit.com/lufthansa.com'),
            ('Air China', 'https://logo.clearbit.com/airchina.com'),
            ('China Eastern Airlines', 'https://logo.clearbit.com/ceair.com'),
            ('Air France', 'https://logo.clearbit.com/airfrance.com'),
            ('British Airways', 'https://logo.clearbit.com/britishairways.com'),
            ('Ryanair', 'https://logo.clearbit.com/ryanair.com'),
            ('Turkish Airlines', 'https://logo.clearbit.com/turkishairlines.com'),
            ('Qatar Airways', 'https://logo.clearbit.com/qatarairways.com'),
            ('IndiGo', 'https://logo.clearbit.com/goindigo.in'),
            ('LATAM Airlines Group', 'https://logo.clearbit.com/latam.com'),
            ('Japan Airlines', 'https://logo.clearbit.com/jal.com'),
            ('ANA (All Nippon Airways)', 'https://logo.clearbit.com/ana.co.jp'),
            ('Cathay Pacific', 'https://logo.clearbit.com/cathaypacific.com'),
            ('Air Canada', 'https://logo.clearbit.com/aircanada.com'),
            ('KLM Royal Dutch Airlines', 'https://logo.clearbit.com/klm.com'),
            ('easyJet', 'https://logo.clearbit.com/easyjet.com'),
            ('Singapore Airlines', 'https://logo.clearbit.com/singaporeair.com'),
            ('Qantas', 'https://logo.clearbit.com/qantas.com'),
            ('Etihad Airways', 'https://logo.clearbit.com/etihad.com'),
            ('Korean Air', 'https://logo.clearbit.com/koreanair.com'),
            ('Aeroflot', 'https://logo.clearbit.com/aeroflot.ru'),
            ('Air India', 'https://logo.clearbit.com/airindia.in'),
            ('Iberia', 'https://logo.clearbit.com/iberia.com'),
            ('Hainan Airlines', 'https://logo.clearbit.com/hainanairlines.com'),
            ('Jet2.com', 'https://logo.clearbit.com/jet2.com'),
            ('Alaska Airlines', 'https://logo.clearbit.com/alaskaair.com'),
            ('Wizz Air', 'https://logo.clearbit.com/wizzair.com'),
            ('JetBlue Airways', 'https://logo.clearbit.com/jetblue.com'),
            ('AirAsia Group', 'https://logo.clearbit.com/airasia.com'),
            ('EVA Air', 'https://logo.clearbit.com/evaair.com'),
            ('Avianca', 'https://logo.clearbit.com/avianca.com'),
            ('SpiceJet', 'https://logo.clearbit.com/spicejet.com'),
            ('Garuda Indonesia', 'https://logo.clearbit.com/garuda-indonesia.com'),
            ('Vueling Airlines', 'https://logo.clearbit.com/vueling.com'),
            ('Thai Airways', 'https://logo.clearbit.com/thaiairways.com'),
            ('SAS Scandinavian Airlines', 'https://logo.clearbit.com/flysas.com'),
            ('TAP Air Portugal', 'https://logo.clearbit.com/flytap.com'),
            ('Aegean Airlines', 'https://logo.clearbit.com/aegeanair.com'),
            ('Pegasus Airlines', 'https://logo.clearbit.com/flypgs.com'),
            ('Norwegian Air Shuttle', 'https://logo.clearbit.com/norwegian.com'),
            ('Aeromexico', 'https://logo.clearbit.com/aeromexico.com'),
            ('Vietnam Airlines', 'https://logo.clearbit.com/vietnamairlines.com'),
            ('Swiss International Air Lines', 'https://logo.clearbit.com/swiss.com'),
            ('Finnair', 'https://logo.clearbit.com/finnair.com');
        """,
        # "Down" SQL statement to delete all airlines
        """--sql
            TRUNCATE TABLE airlines RESTART IDENTITY;
        """,
    ],
]
