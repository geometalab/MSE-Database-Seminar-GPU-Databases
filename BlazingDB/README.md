## Installation
Pull the repository, build the docker container and run the container.

### Docker
```shell
cd dbseminar/BlazingDB
nvida-docker build -t blazingDB .
docker run -d --name blazingDB -p 8890:8890  blazingDB
```
