from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.boarding import Boarding
from models.booking import Booking
from models.flight import Flight
from services.booking_service import checkin_allowed

router = APIRouter(
    tags=["Boarding"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/checkin/{booking_id}")
def checkin(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found."
        )

    flight = db.query(Flight).filter(
        Flight.id == booking.flight_id
    ).first()

    if not checkin_allowed(
        flight.departure_time
    ):
        raise HTTPException(
            status_code=400,
            detail="Check-in is allowed only within 24 hours before departure."
        )

    boarding = Boarding(
        booking_id=booking.id,
        checkin_time=datetime.now(),
        status="Checked In"
    )

    db.add(boarding)
    db.commit()

    return {
        "message": "Check-in completed successfully."
    }


@router.post("/boarding/{booking_id}")
def board_flight(
    booking_id: int,
    db: Session = Depends(get_db)
):

    boarding = db.query(Boarding).filter(
        Boarding.booking_id == booking_id
    ).first()

    if not boarding:
        raise HTTPException(
            status_code=404,
            detail="Passenger has not checked in."
        )

    boarding.boarding_time = datetime.now()
    boarding.status = "Boarded"

    db.commit()

    return {
        "message": "Passenger boarded successfully."
    }


@router.get("/passengers/{passenger_id}/bookings")
def passenger_booking_history(
    passenger_id: int,
    db: Session = Depends(get_db)
):

    bookings = db.query(Booking).filter(
        Booking.passenger_id == passenger_id
    ).all()

    return bookings
