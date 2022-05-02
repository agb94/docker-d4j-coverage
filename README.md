## Docker setup
```bash
git clone https://github.com/agb94/docker-d4j-coverage
cd docker-d4j-coverage/
cd docker/
docker build --tag d4j-cov:latest .
docker run -dt --name d4j-cov -v $(pwd)/resources/workspace:/root/workspace -v $(pwd)/resources/coverage:/root/coverage d4j-cov:latest
```

## Measuring coverage
```bash
docker exec d4j-cov sh /root/workspace/measure_coverage.sh <pid> <vid>b
# ex) docker exec d4j-cov sh /root/workspace/measure_coverage.sh Lang 65b
```
This command will measure the coverage of `<pid>-<vid>b` in Defects4J using Cobertura and save the coverage matrix into `<project_root>/docker/resources/coverage/<pid>-<vid>b.pkl`.
```python
import pandas as pd
df = pd.read_pickle('./docker/resoureces/coverage/<pid>-<vid>b.pkl')
# ex) pd.read_pickle('./docker/resoureces/coverage/Lang-65b.pkl')
```
