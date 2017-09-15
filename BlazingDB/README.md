## Installation
Pull the repository, build the docker container and run the container.

### Docker
```shell
cd dbseminar/BlazingDB
nvida-docker build -t blazingdb .
nvida-docker run -d --name blazingdb -p 8890:8890  blazingdb
```
