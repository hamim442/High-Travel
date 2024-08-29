from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.city_queries import CityQueries, CityDoesNotExist
from models.cities import City, CityRequest

client = TestClient(app)

SEATTLE = {
    "id": 1,
    "name": "Seattle",
    "administrative_division": "Washington",
    "country": "United States",
    "picture_url": "http://www.example.com/seattle.jpg",
    "description": "Lorem ipsum odor amet, consectetuer adipiscing elit.",
}

VANCOUVER = {
    "id": 2,
    "name": "Vancouver",
    "administrative_division": "British Columbia",
    "country": "Canada",
    "picture_url": "http://www.example.com/vancouver.jpg",
    "description": "Lorem ipsum odor amet, consectetuer adipiscing elit.",
}

WHISTLER = {
    "name": "Whistler",
    "administrative_division": "British Columbia",
    "country": "Canada",
    "picture_url": "http://www.example.com/whistler.jpg",
    "description": "Lorem ipsum odor amet, consectetuer adipiscing elit.",
}


class EmptyCityQueries:
    def get_all_cities(self) -> list[City]:
        return []


class MockCityQueries:
    def get_all_cities(self) -> list[City]:
        return [City(**SEATTLE), City(**VANCOUVER)]

    def get_city(self, id: int) -> City:
        if id == 1:
            return City(**SEATTLE)
        raise CityDoesNotExist(f"City {id} does not exist.")

    def search_cities(self, search: str) -> list[City]:
        if search.lower() in SEATTLE["name"].lower():
            return [City(**SEATTLE)]
        elif search.lower() in VANCOUVER["name"].lower():
            return [City(**VANCOUVER)]
        return []

    def create_city(self, city: CityRequest) -> City:
        return City(id=3, **city.model_dump())


class TestCities(TestCase):
    def test_get_all_cities_empty(self):
        app.dependency_overrides[CityQueries] = EmptyCityQueries
        response = client.get("/api/cities")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])
        app.dependency_overrides = {}

    def test_get_all_cities(self):
        app.dependency_overrides[CityQueries] = MockCityQueries
        response = client.get("/api/cities")
        assert response.status_code == 200
        self.assertEqual(response.json(), [SEATTLE, VANCOUVER])
        app.dependency_overrides = {}

    def test_get_city_by_id(self):
        app.dependency_overrides[CityQueries] = MockCityQueries

        response = client.get("/api/cities/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), SEATTLE)

        response = client.get("/api/cities/999")
        assert response.status_code == 404
        self.assertEqual(
            response.json(),
            {"detail": "City 999 does not exist."},
        )

        app.dependency_overrides = {}

    def test_search_city(self):
        app.dependency_overrides[CityQueries] = MockCityQueries

        response = client.get("/api/cities?search=Seattle")
        assert response.status_code == 200
        self.assertEqual(response.json(), [SEATTLE])

        response = client.get("/api/cities?search=NonExistent")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])

        app.dependency_overrides = {}

    def test_create_city(self):
        app.dependency_overrides[CityQueries] = MockCityQueries

        response = client.post("/api/cities/", json=WHISTLER)
        assert response.status_code == 200
        created_city = response.json()
        self.assertEqual(created_city["id"], 3)
        self.assertEqual(created_city["name"], WHISTLER["name"])

        app.dependency_overrides = {}
