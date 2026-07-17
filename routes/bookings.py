from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.booking import Booking
from models.flight import Flight
from schemas.booking import BookingCreate
from services.booking_service import (
    valid_booking_status,
    valid_journey_date,
    seat_available
)

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    flight = db.query(Flight).filter(
        Flight.id == booking.flight_id
    ).first()

    if not flight:
        raise HTTPException(
            status_code=404,
            detail="Flight not found."
        )

    if not valid_journey_date(
        booking.journey_date
    ):
        raise HTTPException(
            status_code=400,
            detail="Journey date cannot be in the past."
        )

    if not valid_booking_status(
        booking.booking_status
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid booking status."
        )

    existing = db.query(Booking).filter(
        Booking.flight_id == booking.flight_id,
        Booking.journey_date == booking.journey_date,
        Booking.seat_number == booking.seat_number,
        Booking.booking_status != "Cancelled"
    ).first()

    if not seat_available(existing):
        raise HTTPException(
            status_code=400,
            detail="Seat already booked."
        )

    db_booking = Booking(**booking.dict())

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    return db_booking


@router.get("/")
def get_bookings(
    status: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Booking)

    if status:
        query = query.filter(
            Booking.booking_status == status
        )

    total = query.count()

    bookings = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": bookings
    }


@router.get("/{booking_id}")
def get_booking(
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

    return booking


@router.put("/{booking_id}")
def update_booking(
    booking_id: int,
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    db_booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not db_booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found."
        )

    db_booking.booking_status = booking.booking_status

    db.commit()

    return {
        "message": "Booking updated successfully."
    }


@router.delete("/{booking_id}")
def cancel_booking(
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

    booking.booking_status = "Cancelled"

    db.commit()

    return {
        "message": "Booking cancelled successfully. Seat released."
    }
