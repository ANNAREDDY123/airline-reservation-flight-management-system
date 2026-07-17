from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.flight import Flight
from schemas.flight import FlightCreate

router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_flight(
    flight: FlightCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Flight).filter(
        Flight.flight_number == flight.flight_number
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Flight number already exists."
        )

    db_flight = Flight(**flight.dict())

    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)

    return db_flight


@router.get("/")
def get_flights(
    source: str = None,
    destination: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Flight)

    if source:
        query = query.filter(
            Flight.source.contains(source)
        )

    if destination:
        query = query.filter(
            Flight.destination.contains(destination)
        )

    total = query.count()

    flights = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": flights
    }


@router.get("/{flight_id}")
def get_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    flight = db.query(Flight).filter(
        Flight.id == flight_id
    ).first()

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="Flight not found."
        )

    return flight


@router.put("/{flight_id}")
def update_flight(
    flight_id: int,
    flight: FlightCreate,
    db: Session = Depends(get_db)
):

    db_flight = db.query(Flight).filter(
        Flight.id == flight_id
    ).first()

    if not db_flight:

        raise HTTPException(
            status_code=404,
            detail="Flight not found."
        )

    duplicate = db.query(Flight).filter(
        Flight.flight_number == flight.flight_number,
        Flight.id != flight_id
    ).first()

    if duplicate:

        raise HTTPException(
            status_code=400,
            detail="Flight number already exists."
        )

    db_flight.flight_number = flight.flight_number
    db_flight.airline_name = flight.airline_name
    db_flight.source = flight.source
    db_flight.destination = flight.destination
    db_flight.departure_time = flight.departure_time
    db_flight.arrival_time = flight.arrival_time
    db_flight.total_seats = flight.total_seats

    db.commit()
    db.refresh(db_flight)

    return db_flight


@router.delete("/{flight_id}")
def delete_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    flight = db.query(Flight).filter(
        Flight.id == flight_id
    ).first()

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="Flight not found."
        )

    db.delete(flight)
    db.commit()

    return {
        "message": "Flight deleted successfully."
    }
