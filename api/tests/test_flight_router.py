from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.flight_queries import FlightQueries, FlightDoesNotExist, FlightCreationError
from models.flights import Flight, FlightRequest

client = TestClient(app)

FLIGHT1 = {
    "id": 1,
    "flight_number": "ABC123",
    "departure_time": "2024-09-01T10:00:00",
    "arrival_time": "2024-09-01T12:00:00",
    "departure_airport": "Airport1",
    "arrival_airport": "Airport2",
    "price": 300,
    "airline_id": 1,
    "trip_id": 1,
}

FLIGHT2 = {
    "id": 2,
    "flight_number": "XYZ456",
    "departure_time": "2024-09-05T14:00:00",
    "arrival_time": "2024-09-05T16:00:00",
    "departure_airport": "Airport3",
    "arrival_airport": "Airport4",
    "price": 450,
    "airline_id": 2,
    "trip_id": 2,
}

FLIGHT_REQUEST = {
    "flight_number": "LMN789",
    "departure_time": "2024-09-10T09:00:00",
    "arrival_time": "2024-09-10T11:00:00",
    "departure_airport": "Airport5",
    "arrival_airport": "Airport6",
    "price": 500,
    "airline_id": 3,
    "trip_id": 3,
}

class EmptyFlightQueries:
    def get_all_flights(self) -> list[Flight]:
        return []

class MockFlightQueries:
    def get_all_flights(self) -> list[Flight]:
        return [Flight(**FLIGHT1), Flight(**FLIGHT2)]

    def get_flight(self, id: int) -> Flight:
        if id == 1:
            return Flight(**FLIGHT1)
        raise FlightDoesNotExist(f"No flight with id {id}.")

    def create_flight(self, flight: FlightRequest) -> Flight:
        return Flight(id=3, **flight.model_dump())

    def delete_flight(self, id: int) -> bool:
        if id == 1:
            return True
        return False

class TestFlights(TestCase):
    def test_get_all_flights_empty(self):
        app.dependency_overrides[FlightQueries] = EmptyFlightQueries
        response = client.get("/api/flights")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])
        app.dependency_overrides = {}

    def test_get_all_flights(self):
        app.dependency_overrides[FlightQueries] = MockFlightQueries
        response = client.get("/api/flights")
        assert response.status_code == 200
        self.assertEqual(response.json(), [FLIGHT1, FLIGHT2])
        app.dependency_overrides = {}

    def test_get_flight_by_id(self):
        app.dependency_overrides[FlightQueries] = MockFlightQueries

        response = client.get("/api/flights/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), FLIGHT1)

        response = client.get("/api/flights/999")
        assert response.status_code == 404
        self.assertEqual(
            response.json(),
            {"detail": "Flight not found"},
        )

        app.dependency_overrides = {}

    def test_create_flight(self):
        app.dependency_overrides[FlightQueries] = MockFlightQueries

        response = client.post("/api/flights/", json=FLIGHT_REQUEST)
        assert response.status_code == 200
        created_flight = response.json()
        self.assertEqual(created_flight["id"], 3)
        self.assertEqual(created_flight["flight_number"], FLIGHT_REQUEST["flight_number"])

        app.dependency_overrides = {}

    def test_delete_flight(self):
        app.dependency_overrides[FlightQueries] = MockFlightQueries

        response = client.delete("/api/flights/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), {"status": "Flight deleted successfully."})

        response = client.delete("/api/flights/999")
        assert response.status_code == 404
        self.assertEqual(response.json(), {"detail": "Flight not found."})

        app.dependency_overrides = {}
