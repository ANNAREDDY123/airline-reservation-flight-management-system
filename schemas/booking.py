from datetime import date

from pydantic import BaseModel, Field


class BookingCreate(BaseModel):

    passenger_id: int

    flight_id: int

    journey_date: date

    seat_number: int = Field(..., gt=0)

    booking_status: str


class BookingResponse(BookingCreate):

    id: int

    class Config:
        from_attributes = True
