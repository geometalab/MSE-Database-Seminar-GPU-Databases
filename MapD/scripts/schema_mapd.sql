DROP TABLE IF EXISTS trips;

CREATE TABLE trips (
  cab_type_id INTEGER,
  passenger_count INTEGER,
  pickup_datetime timestamp,
  dropoff_datetime timestamp,
  pickup_longitude REAL,
  pickup_latitude REAL,
  dropoff_longitude REAL,
  dropoff_latitude REAL,
  trip_distance REAL,
  fare_amount REAL,
  total_amount REAL
);
