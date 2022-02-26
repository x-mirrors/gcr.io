# gcr.io

[![google-containers](https://github.com/x-mirrors/gcr.io/actions/workflows/google-containers.yml/badge.svg?branch=main)](https://github.com/x-mirrors/gcr.io/actions/workflows/google-containers.yml)
[![ml-pipeline](https://github.com/x-mirrors/gcr.io/actions/workflows/ml-pipeline.yml/badge.svg?branch=main)](https://github.com/x-mirrors/gcr.io/actions/workflows/ml-pipeline.yml)

sync google container registry images to hub.docker.com

|  GCR | Docker |
| ------------ | ------------ |
| gcr.io/google-containers | https://hub.docker.com/u/gcmirrors |
| gcr.io/ml-pipeline | https://hub.docker.com/u/mlmirrors |

## generates

```
gcloud container images list --project google-containers
gcloud container images list --project ml-pipeline
```
