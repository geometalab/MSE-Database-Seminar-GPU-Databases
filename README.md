# MSE-Database-Seminar-GPU-Databases
This Repository provides Dockerfiles for a first touch with GPU Databases, 
a Postgres Dockerfile for benchmark purpose and the related queries.

## Queries
For the queries we use the New York City Taxi and Uber data from https://github.com/toddwschneider/nyc-taxi-data .


The queries for the benchmark can be found inside of the Queries directory in the queries.sql file.
The first six queries should be rather fast and the last four ones may take more than an hour.

### Analyze
To analyze the queries Postgres provides some help.
It's a good idea to turn timing on with the command `\timing` in the psql console.  
Furthermore Postgres has the EXPLAIN command (https://www.postgresql.org/docs/9.6/static/sql-explain.html) and
with https://explain.depesz.com/ a nice tool to make the analyzations readable.


## Notes

### Postgres
The Postgres Container additionally has the Postgis extension installed for spatial queries.
And is shipped with tuned configuration parameters for a lot of data (see db-settings.sh file).

### GPU Databases
We created Dockerfiles for:
*  PG-Strom
*  MapD
*  BlazingDB
