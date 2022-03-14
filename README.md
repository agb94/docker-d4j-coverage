## Docker setup
```bash
cd docker/
docker build --tag d4j-cov:latest .
docker run -dt --name d4j-cov -v $(pwd)/resources/workspace:/root/workspace -v $(pwd)/resources/coverage:/root/coverage d4j-cov:latest
```

## Measuring coverage
```bash
docker exec d4j-cov sh /root/workspace/measure_coverage.sh <pid> <vid>b
# ex) docker exec d4j-cov sh /root/workspace/measure_coverage.sh Lang 65b
```
This command will save the coverage matrix into `<project_root>/docker/resources/coverage/<pid>-<vid>b.pkl`.
```python
import pandas as pd
df = pd.read_pickle('./docker/resoureces/coverage/<pid>-<vid>b.pkl')
# ex) pd.read_pickle('./docker/resoureces/coverage/Lang-65b.pkl')
```
