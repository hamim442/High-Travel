from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    auth_router,
    airline_router,
    city_router,
    trip_router,
    stay_router,
    accommodation_router,
    user_trip_router,
    flight_router,
    train_router,
    car_router,
)

import os

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(airline_router.router)
app.include_router(city_router.router)
app.include_router(trip_router.router)
app.include_router(stay_router.router)
app.include_router(accommodation_router.router)
app.include_router(user_trip_router.router)
app.include_router(flight_router.router)
app.include_router(train_router.router)
app.include_router(car_router.router)
