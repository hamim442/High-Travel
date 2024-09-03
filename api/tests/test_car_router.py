from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.car_queries import CarQueries, CarDoesNotExist
from models.cars import Car, CarRequest

client = TestClient(app)

Car1 = {
    "id": 1,
    "car_model": "Model1",
    "rental_company": "Company1",
    "pickup_time": "2024-09-01T10:00:00",
    "dropoff_time": "2024-09-10T10:00:00",
    "pickup_location": "Location1",
    "dropoff_location": "Location2",
    "trip_id": 1,
    "price": 100,
}

Car2 = {
    "id": 2,
    "car_model": "Model2",
    "rental_company": "Company2",
    "pickup_time": "2024-09-05T14:00:00",
    "dropoff_time": "2024-09-15T14:00:00",
    "pickup_location": "Location3",
    "dropoff_location": "Location4",
    "trip_id": 2,
    "price": 150,
}

Car3 = {
    "car_model": "Model3",
    "rental_company": "Company3",
    "pickup_time": "2024-09-10T09:00:00",
    "dropoff_time": "2024-09-20T09:00:00",
    "pickup_location": "Location5",
    "dropoff_location": "Location6",
    "trip_id": 3,
    "price": 200,
}


class EmptyCarQueries:
    def get_all_cars(self) -> list[Car]:
        return []


class MockCarQueries:
    def get_all_cars(self) -> list[Car]:
        return [Car(**Car1), Car(**Car2)]

    def get_car(self, id: int) -> Car:
        if id == 1:
            return Car(**Car1)
        raise CarDoesNotExist(f"Car with id {id} does not exist.")

    def create_car(self, car: CarRequest) -> Car:
        return Car(id=3, **car.model_dump())

    def delete_car(self, id: int) -> bool:
        if id == 1:
            return True
        return False


class TestCars(TestCase):
    def setUp(self):
        self.original_dependency = app.dependency_overrides.get(CarQueries)

    def tearDown(self):
        if self.original_dependency:
            app.dependency_overrides[CarQueries] = self.original_dependency
        else:
            app.dependency_overrides.pop(CarQueries, None)

    def test_get_all_cars_empty(self):
        app.dependency_overrides[CarQueries] = EmptyCarQueries
        response = client.get("/api/cars")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])

    def test_get_all_cars(self):
        app.dependency_overrides[CarQueries] = MockCarQueries
        response = client.get("/api/cars")
        assert response.status_code == 200
        self.assertEqual(response.json(), [Car1, Car2])

    def test_get_car_by_id(self):
        app.dependency_overrides[CarQueries] = MockCarQueries

        response = client.get("/api/cars/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), Car1)

        response = client.get("/api/cars/999")
        assert response.status_code == 404
        self.assertEqual(response.json(), {"detail": "Car not found"})

    def test_create_car(self):
        app.dependency_overrides[CarQueries] = MockCarQueries

        response = client.post("/api/cars/", json=Car3)
        assert response.status_code == 200
        created_car = response.json()
        self.assertEqual(created_car["id"], 3)
        self.assertEqual(created_car["car_model"], Car3["car_model"])

    def test_delete_car(self):
        app.dependency_overrides[CarQueries] = MockCarQueries

        response = client.delete("/api/cars/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), {"status": "Car deleted successfully."})

        response = client.delete("/api/cars/999")
        assert response.status_code == 404
        self.assertEqual(response.json(), {"detail": "Car not found."})
