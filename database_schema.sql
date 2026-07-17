CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(30)
);

CREATE TABLE flights(
    id INTEGER PRIMARY KEY,
    flight_number VARCHAR(50) UNIQUE,
    airline_name VARCHAR(100),
    source VARCHAR(100),
    destination VARCHAR(100),
    departure_time DATETIME,
    arrival_time DATETIME,
    total_seats INTEGER
);

CREATE TABLE bookings(
    id INTEGER PRIMARY KEY,
    passenger_id INTEGER,
    flight_id INTEGER,
    journey_date DATE,
    seat_number INTEGER,
    booking_status VARCHAR(30)
);

CREATE TABLE boarding(
    id INTEGER PRIMARY KEY,
    booking_id INTEGER UNIQUE,
    checkin_time DATETIME,
    boarding_time DATETIME,
    status VARCHAR(30)
);
