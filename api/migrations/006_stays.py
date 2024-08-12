steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE stays (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            logo_picture_url VARCHAR(500) NOT NULL
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
        ('The Ritz-Carlton', 'https://images.pexels.com/photos/16761915/pexels-photo-16761915/free-photo-of-entrance-to-carlton-hotel-cannes-france.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
        ('The Hilton', 'https://images.pexels.com/photos/20147867/pexels-photo-20147867/free-photo-of-hilton-hotel-in-ho-chi-minh-city.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('AirBnb', 'https://images.pexels.com/photos/5077042/pexels-photo-5077042.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Sheraton', 'https://images.pexels.com/photos/19734603/pexels-photo-19734603/free-photo-of-a-skyscraper-sheraton-hotel-against-a-dramatic-sunset-sky.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Holiday Inn', 'https://images.pexels.com/photos/12149151/pexels-photo-12149151.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Mt.Whitney Motel', 'https://images.pexels.com/photos/13993405/pexels-photo-13993405.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Four Seasons Hotel', 'https://images.pexels.com/photos/20758006/pexels-photo-20758006/free-photo-of-four-seasons-hotel-in-madrid-at-night.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Hyatt', 'https://images.pexels.com/photos/15999434/pexels-photo-15999434/free-photo-of-hotel-among-palm-trees.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Burj Al Arab', 'https://images.pexels.com/photos/2041556/pexels-photo-2041556.jpeg?auto=compress&cs=tinysrgb&w=600'),
        ('Hotel Felice', 'https://images.pexels.com/photos/10453855/pexels-photo-10453855.jpeg?auto=compress&cs=tinysrgb&w=600');
        """,
        # "Down" SQL statement
        """--sql
        DELETE FROM stays WHERE id BETWEEN 1 AND 25;
        """,
    ]
]
