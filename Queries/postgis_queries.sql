/* Query 5 */
SELECT *
FROM   trips
WHERE  trips.pickup && St_MakeEnvelope(-74.007511, 40.7105, -73.983479,
                       40.731071, 4326) LIMIT 10;




/* Query 6 average speed of Yellow taxi trips by hour of day in bounding box*/
SELECT Extract(hour FROM pickup_datetime) AS h,
       Avg(Round(trip_distance / NULLIF(Date_part('hour',
                                            dropoff_datetime - pickup_datetime),
                                 0)))
                                         AS speed
FROM   trips
WHERE  (trips.pickup && ST_MakeEnvelope(-74.007511, 40.7105, -73.983479, 40.731071, 4326))
       AND trip_distance > 0
       AND fare_amount / trip_distance BETWEEN 2 AND 10
       AND dropoff_datetime > pickup_datetime
       AND cab_type_id = 1
GROUP  BY h
ORDER  BY h;


/* Query 9 average speed of Yellow taxi trips by day of week in bounding box*/
SELECT Extract(dow FROM pickup_datetime) AS dow,
       Avg(Round(trip_distance / NULLIF(Date_part('hour',
                                            dropoff_datetime - pickup_datetime),
                                 0)))
                                         AS speed
FROM   trips
WHERE  (trips.pickup && ST_MakeEnvelope(-74.007511, 40.7105, -73.983479, 40.731071, 4326))
       AND trip_distance > 0
       AND fare_amount / trip_distance BETWEEN 2 AND 10
       AND dropoff_datetime > pickup_datetime
       AND cab_type_id = 1
GROUP  BY dow
ORDER  BY dow;