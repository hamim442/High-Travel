from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from queries.train_queries import TrainQueries, TrainDoesNotExist
from models.trains import Train, TrainRequest

client = TestClient(app)

Train1 = {
    "id": 1,
    "train_number": "1234",
    "departure_time": "2024-09-01T10:00:00",
    "arrival_time": "2024-09-01T12:00:00",
    "departure_station": "Station A",
    "arrival_station": "Station B",
    "trip_id": 1,
    "price": 100
}

Train2 = {
    "id": 2,
    "train_number": "5678",
    "departure_time": "2024-09-02T14:00:00",
    "arrival_time": "2024-09-02T16:00:00",
    "departure_station": "Station C",
    "arrival_station": "Station D",
    "trip_id": 2,
    "price": 150
}

Train3 = {
    "id": 3,
    "train_number": "91011",
    "departure_time": "2024-09-03T18:00:00",
    "arrival_time": "2024-09-03T20:00:00",
    "departure_station": "Station E",
    "arrival_station": "Station F",
    "trip_id": 3,
    "price": 200
}


class EmptyTrainQueries:
    def get_all_trains(self) -> list[Train]:
        return []


class MockTrainQueries:
    def get_all_trains(self) -> list[Train]:
        return [Train(**Train1), Train(**Train2)]

    def get_train(self, id: int) -> Train:
        if id == 1:
            return Train(**Train1)
        raise TrainDoesNotExist(f"Train with id {id} does not exist.")

    def create_train(self, train: TrainRequest) -> Train:
        return Train(id=3, **train.model_dump())

    def delete_train(self, id: int) -> bool:
        if id == 1:
            return True
        raise TrainDoesNotExist(f"Train with id {id} does not exist.")

    def edit_train(self, train_id: int, **kwargs) -> Train:
        if train_id == 1:
            return Train(id=1, **kwargs)
        raise TrainDoesNotExist(f"Train with id {train_id} does not exist.")


class TestTrains(TestCase):
    def test_get_all_trains_empty(self):
        app.dependency_overrides[TrainQueries] = EmptyTrainQueries
        response = client.get("/api/trains")
        assert response.status_code == 200
        self.assertEqual(response.json(), [])
        app.dependency_overrides = {}

    def test_get_all_trains(self):
        app.dependency_overrides[TrainQueries] = MockTrainQueries
        response = client.get("/api/trains")
        assert response.status_code == 200
        self.assertEqual(response.json(), [Train1, Train2])
        app.dependency_overrides = {}

    def test_get_train_by_id(self):
        app.dependency_overrides[TrainQueries] = MockTrainQueries

        response = client.get("/api/trains/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), Train1)

        response = client.get("/api/trains/999")
        assert response.status_code == 404
        self.assertEqual(
            response.json(),
            {"detail": "Train not found"},
        )

        app.dependency_overrides = {}

    def test_create_train(self):
        app.dependency_overrides[TrainQueries] = MockTrainQueries

        response = client.post("/api/trains/", json=Train3)
        assert response.status_code == 200
        created_train = response.json()
        self.assertEqual(created_train["id"], 3)
        self.assertEqual(created_train["train_number"], Train3["train_number"])

        app.dependency_overrides = {}

    def test_delete_train(self):
        app.dependency_overrides[TrainQueries] = MockTrainQueries

        response = client.delete("/api/trains/1")
        assert response.status_code == 200
        self.assertEqual(response.json(), {"status": "Train deleted successfully."})

        response = client.delete("/api/trains/999")
        assert response.status_code == 404
        self.assertEqual(response.json(), {"detail": "Train not found."})

        app.dependency_overrides = {}
