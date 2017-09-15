## Installation
Pull the repository, build the docker container and run the container.

### Docker
```shell
cd dbseminar/BlazingDB
nvidia-docker build -t blazingdb .
nvidia-docker run -d --name blazingdb -p 8890:8890 -p 40001:40001  blazingdb
```
