from datetime import date
from datetime import datetime
from datetime import timedelta


VALID_STATUS = [
    "Booked",
    "Confirmed",
    "Cancelled",
    "Completed"
]


def valid_booking_status(status: str):

    return status in VALID_STATUS


def valid_journey_date(journey_date):

    return journey_date >= date.today()


def seat_available(existing_booking):

    return existing_booking is None


def checkin_allowed(
    departure_time: datetime
):

    current_time = datetime.now()

    allowed_time = departure_time - timedelta(hours=24)

    return allowed_time <= current_time <= departure_time
