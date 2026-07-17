from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from database import Base


class Flight(Base):

    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)

    flight_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    airline_name = Column(
        String(100),
        nullable=False
    )

    source = Column(
        String(100),
        nullable=False
    )

    destination = Column(
        String(100),
        nullable=False
    )

    departure_time = Column(
        DateTime,
        nullable=False
    )

    arrival_time = Column(
        DateTime,
        nullable=False
    )

    total_seats = Column(
        Integer,
        nullable=False
    )
