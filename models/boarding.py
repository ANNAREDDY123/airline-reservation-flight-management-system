from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from database import Base


class Boarding(Base):

    __tablename__ = "boarding"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        unique=True
    )

    checkin_time = Column(
        DateTime,
        nullable=True
    )

    boarding_time = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String(30),
        default="Pending"
    )
