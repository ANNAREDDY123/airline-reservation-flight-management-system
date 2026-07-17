import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.flights import router as flights_router
from routes.bookings import router as bookings_router
from routes.boarding import router as boarding_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Airline Reservation & Flight Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(flights_router)
app.include_router(bookings_router)
app.include_router(boarding_router)


@app.get("/")
def home():

    logger.info("Application Started Successfully")

    return {
        "message": "Airline Reservation & Flight Management System"
    }
