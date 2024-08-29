# High Travel

### Team Members:

-   Al Hamim
-   Charlie Tucker
-   Gerry Villoslado
-   Jason Chen
-   Maximus Bay

**High Travel** – Your go-to platform for planning your next adventure with ease.

High Travel - because every great trip needs a great plan.
High Travel - your adventure, your way.

### Design

The platform is designed for travelers who want to create and share detailed travel plans, collaborate with others, and explore popular destinations. Users can search for cities, plan their trips with contributors, and view curated recommendations for hotels, restaurants, and places to visit.

### APIs

#### Overview

This API manages travel-related data including accommodations, airlines, cities, stays, trips, and user authentication.

##### Base URL

```
/api
```

##### Authentication

Most endpoints require JWT authentication. Include JWT token in the `Authorization` header.

##### Endpoints

###### Accommodations

```
GET    /accommodations
GET    /accommodations/{id}
POST   /accommodations
DELETE /accommodations/{id}
```

###### Airlines

```
GET    /airlines
GET    /airlines/{id}
POST   /airlines
DELETE /airlines/{id}
```

###### Cities

```
GET    /cities
GET    /cities/random
GET    /cities/{id}
POST   /cities
DELETE /cities/{id}
```

###### Stays

```
GET    /stays
GET    /stays/{id}
POST   /stays
DELETE /stays/{id}
```

###### Trips

```
GET    /trips
GET    /trips/{id}
POST   /trips
DELETE /trips/{id}
```

###### User-Trip

```
POST   /user-trip
GET    /user-trip/{trip_id}
DELETE /user-trip
```

###### Authentication

```
POST   /auth/signup
POST   /auth/signin
GET    /auth/authenticate
DELETE /auth/signout
GET    /auth/check-username/{username}
```

##### Models

-   Accommodation
-   Airline
-   City
-   Stay
-   Trip
-   User
-   UserTrip

##### Error Handling

Uses standard HTTP status codes. Detailed error messages in response body.

### Project Initialization

To enjoy High Travel on your local machine, follow these steps:

1. Clone the repository:
   `git clone https://github.com/yourrepo/high-travel.git`

2. Navigate into the project directory:
   `cd high-travel`

3. Create a Docker volume for the database:
   `docker volume create database_volume`

4. Build and start the application using Docker:
   `docker compose up --build`

5. Once the application is running, got to `localhost:5173`
