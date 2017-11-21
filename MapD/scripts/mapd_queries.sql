/* Query 6 average speed of Yellow taxi trips by hour of day in bounding box*/
SELECT Extract(HOUR FROM pickup_datetime) AS h, AVG(trip_distance / NULLIF(TIMESTAMPDIFF(HOUR,pickup_datetime, dropoff_datetime),0)) AS speed
FROM   trips
WHERE  ( pickup_longitude BETWEEN -74.007511 AND -73.983479 )
       AND ( pickup_latitude BETWEEN 40.7105 AND 40.731071 )
       AND trip_distance > 0
       AND fare_amount / trip_distance BETWEEN 2 AND 10
       AND dropoff_datetime > pickup_datetime
       AND cab_type_id = 1
GROUP  BY h
ORDER  BY h;




/* Query 7 average speed of Yellow taxi trips by hour of day */
SELECT Extract(HOUR FROM pickup_datetime) AS h, Avg(trip_distance / NULLIF(TIMESTAMPDIFF(HOUR, pickup_datetime, dropoff_datetime),0))AS speed
FROM   trips
WHERE  trip_distance > 0
       AND fare_amount / trip_distance BETWEEN 2 AND 10
       AND dropoff_datetime > pickup_datetime
       AND cab_type_id = 1
GROUP  BY h
ORDER  BY h;



/* Query 8 average speed of Yellow taxi trips by day of week*/
SELECT Extract(DOW FROM pickup_datetime) AS dow, Avg(trip_distance / NULLIF(TIMESTAMPDIFF(HOUR,pickup_datetime,  dropoff_datetime), 0)) AS speed
FROM   trips
WHERE  trip_distance > 0
       AND fare_amount / trip_distance BETWEEN 2 AND 10
       AND dropoff_datetime > pickup_datetime
       AND cab_type_id = 1
GROUP  BY dow
ORDER  BY dow;



/* Query 9 average speed of Yellow taxi trips by day of week in bounding box*/
SELECT Extract(DOW FROM pickup_datetime) AS dow, Avg(trip_distance / NULLIF(TIMESTAMPDIFF(HOUR,pickup_datetime,  dropoff_datetime), 0)) AS speed
FROM   trips
WHERE  ( pickup_longitude BETWEEN -74.007511 AND -73.983479 )
       AND ( pickup_latitude BETWEEN 40.7105 AND 40.731071 )
       AND trip_distance > 0
       AND fare_amount / trip_distance BETWEEN 2 AND 10
       AND dropoff_datetime > pickup_datetime
       AND cab_type_id = 1
GROUP  BY dow
ORDER  BY dow;