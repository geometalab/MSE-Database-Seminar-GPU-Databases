## Installation
Pull the repository, build the docker container and run the container.

### Docker
```shell
cd dbseminar/PG-Strom
nvidia-docker build -t pg-strom .
nvidia-docker run -d --name pg-strom pg-strom
```
