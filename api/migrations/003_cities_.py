steps = [
    [
        # "Up" SQL statement
        """--sql
            CREATE TABLE cities (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL,
                administrative_division VARCHAR(200),
                country VARCHAR(100),
                picture_url VARCHAR(300),
                UNIQUE(name, country)
            );
        """,
        # "Down" SQL statement
        """--sql
            DROP TABLE cities;
        """,
    ],
    [
        """--sql
            INSERT INTO cities (name, administrative_division, country, picture_url)
            VALUES
            ('Bangkok', 'Bangkok', 'Thailand', 'https://upload.wikimedia.org/wikipedia/commons/5/5b/Bangkok_skytrain_sunset.jpg'),
            ('Paris', 'Île-de-France', 'France', 'https://upload.wikimedia.org/wikipedia/commons/a/af/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg'),
            ('London', 'England', 'United Kingdom', 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg'),
            ('Dubai', 'Dubai', 'United Arab Emirates', 'https://upload.wikimedia.org/wikipedia/commons/8/83/Dubai_skyline_from_Jumeirah_Beach.jpg'),
            ('Singapore', 'Central Region', 'Singapore', 'https://upload.wikimedia.org/wikipedia/commons/5/57/Singapore_Skyline_at_Dusk.jpg'),
            ('New York City', 'New York', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Lower_Manhattan_skyline_-_June_2017.jpg'),
            ('Kuala Lumpur', 'Federal Territory of Kuala Lumpur', 'Malaysia', 'https://upload.wikimedia.org/wikipedia/commons/6/65/Petronas_Twin_Towers_viewed_from_Menara_KL.JPG'),
            ('Tokyo', 'Tokyo Metropolis', 'Japan', 'https://upload.wikimedia.org/wikipedia/commons/1/18/Tokyo_Tower_and_surrounding_buildings_at_night.jpg'),
            ('Istanbul', 'Istanbul Province', 'Turkey', 'https://upload.wikimedia.org/wikipedia/commons/8/83/Bosphorus_Bridge_%28Istanbul%29.jpg'),
            ('Antalya', 'Antalya Province', 'Turkey', 'https://upload.wikimedia.org/wikipedia/commons/4/47/Antalya_Harbour_view.jpg'),
            ('Seoul', 'Seoul', 'South Korea', 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Seoul_skyline_at_night_%282015%29.jpg'),
            ('Osaka', 'Osaka Prefecture', 'Japan', 'https://upload.wikimedia.org/wikipedia/commons/3/38/Osaka_Castle_02bs3200.jpg'),
            ('Makkah', 'Makkah Province', 'Saudi Arabia', 'https://upload.wikimedia.org/wikipedia/commons/f/f9/Masjid_al-Haram_Mecca_Grand_Mosque.jpg'),
            ('Phuket', 'Phuket Province', 'Thailand', 'https://upload.wikimedia.org/wikipedia/commons/4/49/Patong_Beach_Phuket.jpg'),
            ('Pattaya', 'Chonburi Province', 'Thailand', 'https://upload.wikimedia.org/wikipedia/commons/e/e1/Pattaya_Thailand.jpg'),
            ('Hong Kong', 'Hong Kong Island', 'Hong Kong', 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Hong_Kong_Skyline_Restitch_-_Dec_2007.jpg'),
            ('Milan', 'Lombardy', 'Italy', 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Piazza_Duomo%2C_Milan.jpg'),
            ('Barcelona', 'Catalonia', 'Spain', 'https://upload.wikimedia.org/wikipedia/commons/7/71/Barcelona_Sagrada_Familia_01.jpg'),
            ('Rome', 'Lazio', 'Italy', 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Colosseum_in_Rome%2C_Italy_-_April_2007.jpg'),
            ('Bali', 'Bali', 'Indonesia', 'https://upload.wikimedia.org/wikipedia/commons/6/63/Pura_Ulun_Danu_Bratan%2C_Bali.jpg'),
            ('Las Vegas', 'Nevada', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Welcome_to_Fabulous_Las_Vegas.jpg'),
            ('Shanghai', 'Shanghai Municipality', 'China', 'https://upload.wikimedia.org/wikipedia/commons/c/c2/Shanghai_Skyline_2020.jpg'),
            ('Amsterdam', 'North Holland', 'Netherlands', 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Amsterdam_Canal.jpg'),
            ('Vienna', 'Vienna', 'Austria', 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Schloss_Sch%C3%B6nbrunn_Wien_2014_%28200%29.JPG'),
            ('Los Angeles', 'California', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/8/8c/Los_Angeles_Skyline_from_Griffith_Observatory_2013.jpg'),
            ('Madrid', 'Community of Madrid', 'Spain', 'https://upload.wikimedia.org/wikipedia/commons/7/75/Madrid_skyline_Cuatro_Torres_Business_Area.jpg'),
            ('Berlin', 'Berlin', 'Germany', 'https://upload.wikimedia.org/wikipedia/commons/a/a7/Berlin_Reichstag_dome_with_flag.jpg'),
            ('Prague', 'Prague', 'Czech Republic', 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Prague_Castle_and_Charles_Bridge_2010.jpg'),
            ('Miami', 'Florida', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/5/57/Miami_Skyline_20180129.jpg'),
            ('Munich', 'Bavaria', 'Germany', 'https://upload.wikimedia.org/wikipedia/commons/f/f6/Marienplatz_Muenchen.jpg'),
            ('Florence', 'Tuscany', 'Italy', 'https://upload.wikimedia.org/wikipedia/commons/6/6a/Florence_Cathedral_from_Michelangelo_square.jpg'),
            ('Sydney', 'New South Wales', 'Australia', 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Sydney_Opera_House_viewed_from_Harbour_Bridge.jpg'),
            ('Buenos Aires', 'Autonomous City of Buenos Aires', 'Argentina', 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Buenos_Aires_-_Recoleta.jpg'),
            ('San Francisco', 'California', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/0/0c/San_Francisco_-_Golden_Gate_Bridge_and_Cityscape.jpg'),
            ('Mexico City', 'Mexico City', 'Mexico', 'https://upload.wikimedia.org/wikipedia/commons/4/41/Angel_of_Independence_Mexico_City.jpg'),
            ('Moscow', 'Moscow', 'Russia', 'https://upload.wikimedia.org/wikipedia/commons/d/d1/RedSquareMoscow.jpg'),
            ('Toronto', 'Ontario', 'Canada', 'https://upload.wikimedia.org/wikipedia/commons/c/c6/Toronto_skyline_at_night_-a.jpg'),
            ('Orlando', 'Florida', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/5/58/Walt_Disney_World_-_Disney%27s_Animal_Kingdom_-_Tree_of_Life_%281%29.jpg'),
            ('Rio de Janeiro', 'Rio de Janeiro', 'Brazil', 'https://upload.wikimedia.org/wikipedia/commons/4/41/Rio_de_Janeiro.jpg'),
            ('Beijing', 'Beijing Municipality', 'China', 'https://upload.wikimedia.org/wikipedia/commons/a/af/Beijing_Skyline_CBD_2016.jpg'),
            ('Cape Town', 'Western Cape', 'South Africa', 'https://upload.wikimedia.org/wikipedia/commons/a/a7/Cape_Town_and_Table_Mountain.jpg'),
            ('Lisbon', 'Lisbon District', 'Portugal', 'https://upload.wikimedia.org/wikipedia/commons/e/e3/Lisbon_Cityscape_from_Castle_of_S%C3%A3o_Jorge.jpg'),
            ('Venice', 'Veneto', 'Italy', 'https://upload.wikimedia.org/wikipedia/commons/0/00/Venice_Grand_Canal.jpg'),
            ('Brussels', 'Brussels', 'Belgium', 'https://upload.wikimedia.org/wikipedia/commons/6/60/Grand_Place_Brussels_Evening.jpg'),
            ('Cairo', 'Cairo Governorate', 'Egypt', 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Cairo_City_Skyline_2021.jpg'),
            ('Zurich', 'Zurich', 'Switzerland', 'https://upload.wikimedia.org/wikipedia/commons/7/75/Zurich_Cityscape.jpg'),
            ('Mumbai', 'Maharashtra', 'India', 'https://upload.wikimedia.org/wikipedia/commons/6/6e/Mumbai_Skyline_at_night.jpg'),
            ('Delhi', 'National Capital Territory', 'India', 'https://upload.wikimedia.org/wikipedia/commons/a/a2/India_Gate_in_New_Delhi_03-2016.jpg'),
            ('Copenhagen', 'Capital Region', 'Denmark', 'https://upload.wikimedia.org/wikipedia/commons/a/af/Nyhavn_Copenhagen.jpg');
        """,
        """--sql
            DROP TABLE cities;
        """,
    ],
]
