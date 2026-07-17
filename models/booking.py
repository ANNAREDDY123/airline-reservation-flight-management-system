from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ForeignKey

from database import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    passenger_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    flight_id = Column(
        Integer,
        ForeignKey("flights.id")
    )

    journey_date = Column(
        Date,
        nullable=False
    )

    seat_number = Column(
        Integer,
        nullable=False
    )

    booking_status = Column(
        String(30),
        default="Booked"
    )
