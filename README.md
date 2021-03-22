# workflow-repository
Repository of workflows available in usegalaxy.be.

To install these set in your Galaxy instance using ephemeris run:
```
find . -name '*.ga' -exec workflow-install --publish_workflows -w {} -g $GALAXY_URL -a $API_KEY \;
```
In the near future all workflows in this repo should be registered in workflowhub.eu, packaged using RO-Crate together with corresponding metadata: autorship, which instances of Galaxy have them available for usage, etc.

Some of these workflows are tested regularly in our instance for benchmarking/status purposes, check: https://github.com/usegalaxy-be/workflow-testing

The Galaxy Training Network workflows (GTN) are up to date with release [2021-02-01](https://github.com/galaxyproject/training-material/releases/tag/2020-04-01).
