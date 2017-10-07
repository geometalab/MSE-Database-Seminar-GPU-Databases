/* Query 5 */
SELECT *
FROM   trips
WHERE  trips.pickup && St_MakeEnvelope(-74.007511, 40.7105, -73.983479,
                       40.731071, 4326);