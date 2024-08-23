import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRIPADVISOR_API_KEY = os.getenv("TRIPADVISOR_API_KEY")
BASE_URL = "https://api.content.tripadvisor.com/api/v1/location"


def search_location(city_name, country_name, category):
    """
    Search for locations by city, country, and category (hotels, restaurants, attractions).
    Concatenates city and country for better accuracy in search query.
    """
    search_query = f"{city_name}, {country_name}"
    url = f"{BASE_URL}/search"
    headers = {"accept": "application/json"}
    params = {
        "key": TRIPADVISOR_API_KEY,
        "searchQuery": search_query,
        "category": category,
        "language": "en",
        "limit": 10,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None


def get_location_details(location_id):
    """Get details for specific location by its Location ID."""
    url = f"{BASE_URL}/{location_id}/details"
    headers = {"accept": "application/json"}
    params = {"key": TRIPADVISOR_API_KEY, "language": "en"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None


def get_location_photos(location_id, limit=5):
    """Get up to 5 photos for a specific location by its Location ID."""
    url = f"{BASE_URL}/{location_id}/photos"
    headers = {"accept": "application/json"}
    params = {
        "key": TRIPADVISOR_API_KEY,
        "limit": limit,
        "language": "en",
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None
