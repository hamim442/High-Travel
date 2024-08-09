steps = [
    [
        # "Up" SQL statement
        """--sql
        CREATE TABLE cities (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            administrative_division VARCHAR(200),
            country VARCHAR(100),
            picture_url VARCHAR(300)
        );
        """,
        # "Down" SQL statement
        """--sql
        DROP TABLE cities;
        """,
    ],
    [
        """--sql
        INSERT INTO cities (name, administrative_division, country, picture_url) VALUES
            ('Tokyo', 'Tokyo Metropolis', 'Japan', 'https://example.com/tokyo.jpg'),
            ('Delhi', 'National Capital Territory', 'India', 'https://example.com/delhi.jpg'),
            ('Shanghai', 'Shanghai Municipality', 'China', 'https://example.com/shanghai.jpg'),
            ('São Paulo', 'São Paulo', 'Brazil', 'https://example.com/sao_paulo.jpg'),
            ('Mexico City', 'Mexico City', 'Mexico', 'https://example.com/mexico_city.jpg'),
            ('Cairo', 'Cairo Governorate', 'Egypt', 'https://example.com/cairo.jpg'),
            ('Dhaka', 'Dhaka Division', 'Bangladesh', 'https://example.com/dhaka.jpg'),
            ('Mumbai', 'Maharashtra', 'India', 'https://example.com/mumbai.jpg'),
            ('Beijing', 'Beijing Municipality', 'China', 'https://example.com/beijing.jpg'),
            ('Osaka', 'Osaka Prefecture', 'Japan', 'https://example.com/osaka.jpg'),
            ('Karachi', 'Sindh', 'Pakistan', 'https://example.com/karachi.jpg'),
            ('Chongqing', 'Chongqing Municipality', 'China', 'https://example.com/chongqing.jpg'),
            ('Istanbul', 'Istanbul Province', 'Turkey', 'https://example.com/istanbul.jpg'),
            ('Buenos Aires', 'Autonomous City of Buenos Aires', 'Argentina', 'https://example.com/buenos_aires.jpg'),
            ('Kolkata', 'West Bengal', 'India', 'https://example.com/kolkata.jpg'),
            ('Kinshasa', 'Kinshasa', 'Democratic Republic of the Congo', 'https://example.com/kinshasa.jpg'),
            ('Lagos', 'Lagos State', 'Nigeria', 'https://example.com/lagos.jpg'),
            ('Manila', 'Metro Manila', 'Philippines', 'https://example.com/manila.jpg'),
            ('Rio de Janeiro', 'Rio de Janeiro', 'Brazil', 'https://example.com/rio_de_janeiro.jpg'),
            ('Guangzhou', 'Guangdong', 'China', 'https://example.com/guangzhou.jpg'),
            ('Los Angeles', 'California', 'United States', 'https://example.com/los_angeles.jpg'),
            ('Moscow', 'Moscow', 'Russia', 'https://example.com/moscow.jpg'),
            ('Shenzhen', 'Guangdong', 'China', 'https://example.com/shenzhen.jpg'),
            ('Lahore', 'Punjab', 'Pakistan', 'https://example.com/lahore.jpg'),
            ('Bangalore', 'Karnataka', 'India', 'https://example.com/bangalore.jpg');
        """,

        """--sql
        DROP TABLE cities;
        """,
    ]
]
