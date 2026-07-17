# airline-reservation-flight-management-system
FastAPI Airline Reservation &amp; Flight Management System with JWT Authentication, Flight Management, Flight Booking, Boarding Management, Reports, Search, SQLAlchemy ORM, Pagination, Logging, Docker Support, and Unit Tests.
# Airline Reservation & Flight Management System

## Features

- JWT Authentication
- Role-Based Authorization
- Flight Management (CRUD)
- Flight Booking
- Boarding Management
- Search & Reports
- SQLAlchemy ORM
- SQLite Database
- Docker Support
- Logging
- Unit Test Structure



## Installation


pip install -r requirements.txt


## Run Project


uvicorn main:app --reload


Swagger UI:

http://127.0.0.1:8000/docs


## Environment Variables


DATABASE_URL=sqlite:///./airline.db
SECRET_KEY=airline_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440


## API Modules

- Authentication
- Flight Management
- Booking Management
- Boarding Management
- Reports & Search



## Docker


docker build -t airline-system .
docker run -p 8000:8000 airline-system


## Business Rules

- Flight number must be unique.
- Seat cannot be booked twice for the same flight and journey date.
- Journey date cannot be in the past.
- Check-in allowed only within 24 hours before departure.
- Cancelled bookings release the seat automatically.
