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
        return [Airline(**american_airlines), Airline(**delta_airlines)]
