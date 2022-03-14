```bash

cd docker/
# build a docker image
docker build --tag d4j-cov:latest .
# create a docker container in the background
docker run -dt --name d4j-cov -v $(pwd)/resources/workspace:/root/workspace -v $(pwd)/resources/coverage:/root/coverage d4j-cov:latest
# execute an interactive bash shell on the container
# docker exec -it d4j-cov bash
```

# Measuring coverage of a bug in Defects4J
```bash
docker exec d4j-cov sh /root/workspace/measure_coverage.sh <pid> <vid>b
# ex) docker exec d4j-cov sh /root/workspace/measure_coverage.sh Lang 65b
```
This command will save the coverage matrix into `<project_root>/docker/resources/coverage/<pid>-<vid>b`.
```python
import pandas as pd
df = pd.read_pickle('./docker/resoureces/coverage/<pid>-<vid>b')
# ex) pd.read_pickle('./docker/resoureces/coverage/Lang-65b')
```

