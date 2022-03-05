# gcr.io

[![sync](https://github.com/x-mirrors/gcr.io/actions/workflows/sync.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/sync.yml)

sync google container registry images to hub.docker.com

|  GCR | Docker |
| ------------ | ------------ |
| k8s.gcr.io | [gcmirrors](https://hub.docker.com/u/gcmirrors) |
| k8s.gcr.io/scheduler-plugins | [k8sgcrioschedulerplugins](https://hub.docker.com/u/k8sgcrioschedulerplugins) |
| gcr.io/ml-pipeline | [gcriomlpipeline](https://hub.docker.com/u/gcriomlpipeline) |
| gcr.io/google-samples | [gcriogooglesamples](https://hub.docker.com/u/gcriogooglesamples) |

## sync request

- create issue in this repo
- send request to `me@xiexianbin.cn`

## generates

```
# gcloud container images list --project google-containers
gcloud container images list --repository us.gcr.io/k8s-artifacts-prod | awk -F "/" '{print "k8s.gcr.io/"$3}'
gcloud container images list --repository k8s.gcr.io/scheduler-plugins
gcloud container images list --repository k8s.gcr.io/coredns
gcloud container images list --project ml-pipeline
gcloud container images list --repository gcr.io/google-samples
```

## ref

- https://github.com/kubernetes/k8s.io/blob/main/k8s.gcr.io/Vanity-Domain-Flip.md
