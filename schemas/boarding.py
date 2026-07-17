from datetime import datetime

from pydantic import BaseModel


class BoardingCreate(BaseModel):

    booking_id: int


class BoardingResponse(BaseModel):

    id: int

    booking_id: int

    checkin_time: datetime | None = None

    boarding_time: datetime | None = None

    status: str

    class Config:
        from_attributes = True
