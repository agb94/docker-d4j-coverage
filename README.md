```bash
cd docker/
# build a docker image
docker build --tag d4j-cov:latest .
# create a docker container in the background
docker run -dt --name d4j-cov -v $(pwd)/resources/workspace:/root/workspace -v $(pwd)/resources/coverage:/root/coverage d4j-cov:latest
# execute an interactive bash shell on the container
docker exec -it d4j-cov bash
```