# workflow-repository
Repository of workflows available in usegalaxy.be.

To install these set in your Galaxy instance using ephemeris:
```
find . -name '*.ga' -exec workflow-install --publish_workflows -w {} -g $GALAXY_URL -a $API_KEY \;
```
In the near future all workflows in this repo should be registered in workflowhub.eu, packaged using RO-Crate together with corresponding metadata: autorship, which instances of Galaxy have them available for usage, etc.
