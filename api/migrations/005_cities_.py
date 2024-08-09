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
            ('Tokyo', 'Tokyo Metropolis', 'Japan', 'https://media.istockphoto.com/id/1390815938/photo/tokyo-city-in-japan.webp?b=1&s=170667a&w=0&k=20&c=YVI8iGWf-w_cLyQNcWA57Ll9eXv_s_SHfoM0MufEMMQ='),
            ('Delhi', 'National Capital Territory', 'India', 'https://media.cnn.com/api/v1/images/stellar/prod/181105110720-03-delhi-india-what-to-see-photos-swaminarayan-akshardham.jpg?q=w_1920,h_1080,x_0,y_0,c_fill'),
            ('Shanghai', 'Shanghai Municipality', 'China', 'https://static.independent.co.uk/2023/08/07/12/iStock-587787576%20shanghai.jpg?width=1200&height=1200&fit=crop'),
            ('São Paulo', 'São Paulo', 'Brazil', 'https://www.thesmoothescape.com/wp-content/uploads/2019/03/Sao-Paulo-skyline-header.jpg'),
            ('Mexico City', 'Mexico City', 'Mexico', 'https://www.fodors.com/wp-content/uploads/2021/05/UltimateMexicoCity__HERO_shutterstock_1058054480.jpg'),
            ('Cairo', 'Cairo Governorate', 'Egypt', 'https://images.adsttc.com/media/images/64a2/cdae/cb9c/464f/a63a/9764/large_jpg/cairo-architecture-city-guide-exploring-the-unique-architectural-blend-of-historical-and-contemporary-in-egypts-bustling-capital_23.jpg?1688391095'),
            ('Dhaka', 'Dhaka Division', 'Bangladesh', 'https://cdn.britannica.com/97/189797-050-1FC0041B/Night-view-Dhaka-Bangladesh.jpg'),
            ('Mumbai', 'Maharashtra', 'India', 'https://static01.nyt.com/images/2024/04/06/travel/28hours-mumbai-01-qkwb/28hours-mumbai-01-qkwb-videoSixteenByNine3000.jpg'),
            ('Beijing', 'Beijing Municipality', 'China', 'https://www.tripsavvy.com/thmb/kcIwUgDXnduZ9k4ljo4K2eA87M4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/forbidden-city-beijing-8775c18670bd412d9b54daecba137c5c.jpg'),
            ('Osaka', 'Osaka Prefecture', 'Japan', 'https://blog.sakura.co/wp-content/uploads/2023/03/Sakuraco_osaka6-1.jpg'),
            ('Karachi', 'Sindh', 'Pakistan', 'https://oshkoshnorthstar.org/wp-content/uploads/2020/11/Karachi-1.jpg'),
            ('Chongqing', 'Chongqing Municipality', 'China', 'https://facts.net/wp-content/uploads/2023/06/31-facts-about-chongqing-1688111338.jpeg'),
            ('Istanbul', 'Istanbul Province', 'Turkey', 'https://imageio.forbes.com/specials-images/imageserve/61730c93fc56ba9cc0b0c7f2/Blue-Mosque-in-Istanbul/960x0.jpg?format=jpg&width=960'),
            ('Buenos Aires', 'Autonomous City of Buenos Aires', 'Argentina', 'https://www.travelandleisure.com/thmb/zvWBxyJ3Nj56uHYXH73NXXgC3iA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/world-class-design-buenos-aires-BAVISIT0418-5e990a610aab499bb9991771dac5fb54.jpg'),
            ('Kolkata', 'West Bengal', 'India', 'https://cdn.britannica.com/91/110191-050-7BCFD56B/Victoria-Memorial-Hall-Kolkata-India.jpg'),
            ('Kinshasa', 'Kinshasa', 'Democratic Republic of the Congo', 'https://upload.wikimedia.org/wikipedia/commons/b/b9/La_ville_de_Kinshasa.jpg'),
            ('Lagos', 'Lagos State', 'Nigeria', 'https://media.newyorker.com/photos/5909523dc14b3c606c103bac/master/pass/Victoria-Island-580.jpg'),
            ('Manila', 'Metro Manila', 'Philippines', 'https://cdn.audleytravel.com/2559/1828/79/1015820-manila-skyline.jpg'),
            ('Rio de Janeiro', 'Rio de Janeiro', 'Brazil', 'https://i.natgeofe.com/n/560b293d-80b2-4449-ad6c-036a249d46f8/rio-de-janeiro-travel_3x4.jpg'),
            ('Guangzhou', 'Guangdong', 'China', 'https://cdn.britannica.com/12/128212-050-85240B92/Nighttime-view-Guangzhou-Guangdong-China.jpg'),
            ('Los Angeles', 'California', 'United States', 'https://a.travel-assets.com/findyours-php/viewfinder/images/res70/475000/475464-Los-Angeles.jpg'),
            ('Moscow', 'Moscow', 'Russia', 'https://content.r9cdn.net/rimg/dimg/b0/1c/7746c81c-city-14713-163f5192361.jpg?width=1366&height=768&xhint=1535&yhint=594&crop=true'),
            ('Shenzhen', 'Guangdong', 'China', 'https://content.r9cdn.net/rimg/dimg/d6/b4/fd470797-city-9007-16886833eb0.jpg?width=1366&height=768&xhint=2474&yhint=1921&crop=true'),
            ('Lahore', 'Punjab', 'Pakistan', 'https://mediaim.expedia.com/destination/1/7d01ed01c22a1685a1f2046a37ac7f1f.jpg'),
            ('Bangalore', 'Karnataka', 'India', 'https://i.kinja-img.com/image/upload/c_fill,h_900,q_60,w_1600/1432fedb88c0d1cc56f4c496a80f251c.jpg');
        """,

        """--sql
        DROP TABLE cities;
        """,
    ]
]
