## Installation
Pull the repository, build the docker container and run the container.

### Docker
```shell
cd dbseminar/PG-Strom
nvidia-docker build -t pg-strom .
nvidia-docker run -d --name pg-strom pg-strom
```

### Access Postgres
```shell
psql -h localhost -p 5432 -U postgres
postgres=# CREATE EXTENSION pg_strom;
postgres=# \dx
```
