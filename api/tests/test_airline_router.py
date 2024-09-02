from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.airline_queries import AirlineQueries, AirlineDoesNotExist
from models.airlines import Airline, AirlineRequest

client = TestClient(app)


american_airlines = {
    "id": 1,
    "name": "American Airlines",
    "logo_picture_url": "https://logo.clearbit.com/americanairlines.com",
}

delta_airlines = {
    "id": 2,
    "name": "Delta Air Lines",
    "logo_picture_url": "https://logo.clearbit.com/delta.com",
}

united_airliines = {
    "id": 3,
    "name": "United Airlines",
    "logo_picture_url": "https://logo.clearbit.com/united.com",
}


class EmptyAirlineQueries:
    def get_all_airlines(self) -> list[Airline]:
        return []
        # return [Airline(**american_airlines), Airline(**delta_airlines)]


class MockAirlinesQueries:
    def get_all_airlines(self) -> list[Airline]:
        return [Airline(**american_airlines), Airline(**delta_airlines)]

    def get_airline(self, id: int) -> Airline:
        if id == 1:
            return Airline(**american_airlines)
        raise AirlineDoesNotExist(f"Airline {id} does not exist")

    def create_airline(self, airline: AirlineRequest) -> Airline:
        return Airline(id=3, **airline.model_dump())


class TestAirlines(TestCase):
    def test_get_all_airlines_empty(self):
        # Arrange
        app.dependency_overrides[AirlineQueries] = EmptyAirlineQueries
        # Act
        response = client.get("/api/airlines")
        # Assert
        assert response.status_code == 200
        self.assertEqual(response.json(), [])
        app.dependency_overrides = {}

    def test_get_all_airlines(self):
        app.dependency_overrides[AirlineQueries] = MockAirlinesQueries
        response = client.get("/api/airlines")
        assert response.status_code == 200
        self.assertEqual(response.json(), [american_airlines, delta_airlines])
        app.dependency_overrides = {}

    def test_get_airlines_by_id(self):
        app.dependency_overrides[AirlineQueries] = MockAirlinesQueries

        response = client.get("/api/airlines/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), american_airlines)

        response = client.get("/api/airlines/987")
        assert response.status_code == 404
        self.assertEqual(response.json(), {"detail": "Airline not found."})
        app.dependency_overrides = {}

    def test_create_airline(self):
        app.dependency_overrides[AirlineQueries] = MockAirlinesQueries

        response = client.post("/api/airlines", json=united_airliines)
        assert response.status_code == 200
        created_airline = response.json()
        self.assertEqual(created_airline["id"], 3)
        self.assertEqual(created_airline["name"], united_airliines["name"])

        app.dependency_overrides = {}
