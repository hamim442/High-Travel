from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.trip_queries import TripQueries, TripDoesNotExist
from models.trips import Trip, TripRequest
from utils.authentication import hash_password
from models.users import UserWithPw
from typing import Optional
from queries.user_queries import UserQueries

fakePassword = "password"
fakePasswordHash = hash_password(fakePassword)

fakeUser = {
    "id": 1,
    "username": "testuser",
    "password": fakePasswordHash,
    "email": "testuser@unittest.com",
    "first_name": "jay",
    "last_name": "cross",
    "profile_image": "123.jpg",
}

fakeTrip = {
    "id": 1,
    "city_id": 1,
    "start_date": "2020-03-03T00:00:00",
    "end_date": "2020-03-09T00:00:00",
    "user_id": 1,
}

fakeTrip1 = {
    "id": 1,
    "city_id": 1,
    "start_date": "2020-03-03T00:00:00",
    "end_date": "2020-03-09T00:00:00",
    "user_id": 1,
}

fakeTrip2 = {
    "id": 2,
    "city_id": 2,
    "start_date": "2020-02-02T00:00:00",
    "end_date": "2020-02-09T00:00:00",
    "user_id": 1,
}

weeTrip = {
    "city_id": 3,
    "start_date": "2020-03-03T00:00:00",
    "end_date": "2020-02-09T00:00:00",
}


class FakeUserQueries:
    def get_by_username(self, id: int) -> Optional[UserWithPw]:
        return UserWithPw(**fakeUser)


class emptyTripQueries:
    def get_user_trips(self, user_id: int) -> list[Trip]:
        return []


class MockTripQueries:
    def get_user_trips(self, user_id: int) -> list[Trip]:
        return [Trip(**fakeTrip1), Trip(**fakeTrip2)]

    def get_trip(self, trip: TripRequest, user_id: int) -> Trip:
        if id == 1:
            return Trip(**fakeTrip1)
        raise TripDoesNotExist(f"Trip {id} does not exist")

    def create_trip(self, trip: TripRequest, user_id: int) -> Trip:
        print("We made it")
        return Trip(id=3, user_id=1, **trip.model_dump())


class TestTrips(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_user_trips_empty(self):
        app.dependency_overrides[UserQueries] = FakeUserQueries
        app.dependency_overrides[TripQueries] = emptyTripQueries
        self.client.post(
            "/api/auth/signin",
            json={"username": "testuser", "password": fakePassword},
        )

        response = self.client.get("/api/trips")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])
        app.dependency_overrides = {}

    def test_get_user_trips(self):
        app.dependency_overrides[UserQueries] = FakeUserQueries
        app.dependency_overrides[TripQueries] = MockTripQueries
        self.client.post(
            "/api/auth/signin",
            json={"username": "testuser", "password": fakePassword},
        )
        response = self.client.get("/api/trips")
        assert response.status_code == 200
        self.assertEqual(response.json(), [fakeTrip1, fakeTrip2])
        app.dependency_overrides = {}

    def test_create_trip(self):
        app.dependency_overrides[UserQueries] = FakeUserQueries
        app.dependency_overrides[TripQueries] = MockTripQueries
        self.client.post(
            "/api/auth/signin",
            json={"username": "testuser", "password": fakePassword},
        )
        response = self.client.post("/api/trips/", json=weeTrip)
        assert response.status_code == 200
        created_trip = response.json()
        self.assertEqual(created_trip["id"], 3)
        self.assertEqual(created_trip["city_id"], weeTrip["city_id"])

        app.dependency_overrides = {}
