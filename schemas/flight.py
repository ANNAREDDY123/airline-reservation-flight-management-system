from datetime import datetime

from pydantic import BaseModel, Field


class FlightCreate(BaseModel):

    flight_number: str = Field(..., min_length=2, max_length=20)

    airline_name: str = Field(..., min_length=2, max_length=100)

    source: str = Field(..., min_length=2, max_length=100)

    destination: str = Field(..., min_length=2, max_length=100)

    departure_time: datetime

    arrival_time: datetime

    total_seats: int = Field(..., gt=0)


class FlightResponse(FlightCreate):

    id: int

    class Config:
        from_attributes = True
