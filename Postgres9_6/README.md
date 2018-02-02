# Usage
Steps to execute the benchmark.
```
docker build -t <image_name> .
docker run --name <container_name> -v /<data_dir>:/<data_dir> -e POSTGRES_PASSWORD=mysecretpassword -d <image_name>
docker exec -it <container_name> bash
su postgres -c /<data_dir>/nyc-taxi-data/initialize_database.sh
su postgres -c /<data_dir>/nyc-taxi-data/import_trip_data_small.sh
psql -U postgres
\c nyc-taxi-data
\timing
```

### Prewarm
```
psql -U postgres
\c nyc-taxi-data
CREATE EXTENSION pre_warm;
select pg_prewarm('trips','buffer')
```
