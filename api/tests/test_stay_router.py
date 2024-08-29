from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.stay_queries import StayQueries, StayDoesNotExist
from models.stays import Stay, StayRequest

client = TestClient(app)

Hotel1 = {
    "id": 1,
    "name": "Hotel1",
    "logo_picture_url": "http://www.example.com/hotel1.jpg",
}

Hotel2 = {
    "id": 2,
    "name": "Hotel2",
    "logo_picture_url": "http://www.example.com/hotel2.jpg",
}

Hotel3 = {
    "id": 3,
    "name": "Hotel3",
    "logo_picture_url": "http://www.example.com/hotel3.jpg",
}

class EmptyStayQueries:
    def get_all_stays(self) -> list[Stay]:
        return []


class MockStayQueries:
    def get_all_stays(self) -> list[Stay]:
        return [Stay(**Hotel1), Stay(**Hotel2)]

    def get_stay(self, id: int) -> Stay:
        if id == 1:
            return Stay(**Hotel1)
        raise StayDoesNotExist(f"Stay {id} does not exist.")

    def create_stay(self, stay: StayRequest) -> Stay:
        print("Hey inside method")
        return Stay(id=3, **stay.model_dump())


class TestStays(TestCase):
    def test_get_all_stays_empty(self):
        app.dependency_overrides[StayQueries] = EmptyStayQueries
        response = client.get("/api/stays")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])
        app.dependency_overrides = {}

    def test_get_all_stays(self):
        app.dependency_overrides[StayQueries] = MockStayQueries
        response = client.get("/api/stays")
        assert response.status_code == 200
        self.assertEqual(response.json(), [Hotel1, Hotel2])
        app.dependency_overrides = {}

    def test_get_stay_by_id(self):
        app.dependency_overrides[StayQueries] = MockStayQueries

        response = client.get("/api/stays/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), Hotel1)

        response = client.get("/api/stays/999")
        assert response.status_code == 404
        self.assertEqual(
            response.json(),
            {"detail": "stay not found."},
        )

        app.dependency_overrides = {}

    def test_create_stay(self):
        app.dependency_overrides[StayQueries] = MockStayQueries

        response = client.post("/api/stays/", json=Hotel3)
        assert response.status_code == 200
        created_stay = response.json()
        self.assertEqual(created_stay["id"], 3)
        self.assertEqual(created_stay["name"], Hotel3["name"])

        app.dependency_overrides = {}
