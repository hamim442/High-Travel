from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    auth_router,
    airline_router,
    city_router,
    trip_router,
    stay_router,
    accommodation_router,
)

import os

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


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }
