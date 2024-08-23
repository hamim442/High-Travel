from fastapi import APIRouter, Query
from utils.tripadvisor_api import (
    search_location,
    get_location_details,
    get_location_photos,
)

router = APIRouter()


@router.get("/tripadvisor/attractions")
async def get_attractions(city: str = Query(...), country: str = Query(...)):
    data = search_location(city, country, "attractions")
    print(f"TripAdvisor Attractions Response: {data}")  # Log response
    if data:
        attractions = data.get("data", [])
        print(f"Parsed Attractions Data: {attractions}")  # Log parsed data

        for attraction in attractions:
            details = get_location_details(attraction["location_id"])
            print(f"Attraction Details: {details}")  # Log details
            attraction["details"] = details

            photos = get_location_photos(attraction["location_id"])
            if photos:
                attraction["photo_url"] = photos["data"][0]["images"]["large"][
                    "url"
                ]

        return attractions
    return {"error": "Unable to fetch attractions"}


@router.get("/tripadvisor/hotels")
async def get_hotels(city: str = Query(...), country: str = Query(...)):
    data = search_location(city, country, "hotels")
    if data:
        hotels = data["data"]

        for hotel in hotels:
            details = get_location_details(hotel["location_id"])
            hotel["details"] = details

            photos = get_location_photos(hotel["location_id"])
            if photos:
                hotel["photo_url"] = photos["data"][0]["images"]["large"][
                    "url"
                ]  # get the first photo URL

        return hotels
    return {"error": "Unable to fetch hotels"}


@router.get("/tripadvisor/restaurants")
async def get_restaurants(city: str = Query(...), country: str = Query(...)):
    data = search_location(city, country, "restaurants")
    if data:
        restaurants = data["data"]

        for restaurant in restaurants:
            details = get_location_details(restaurant["location_id"])
            restaurant["details"] = details

            photos = get_location_photos(restaurant["location_id"])
            if photos:
                restaurant["photo_url"] = photos["data"][0]["images"]["large"][
                    "url"
                ]  # get the first photo URL

        return restaurants
    return {"error": "Unable to fetch restaurants"}
