# gcr.io

sync google/quay container registry images to hub.docker.com

search which image mirrors online: https://mirrors.kb.cx

- GCR

|  GCR | Docker | Status |
| ------------ | ------------ | ------------ |
| k8s.gcr.io | [gcmirrors](https://hub.docker.com/u/gcmirrors) | [![k8s](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.yml) |
| k8s.gcr.io/coredns | [gcmirrors](https://hub.docker.com/u/gcmirrors) | [![coredns](https://github.com/x-mirrors/gcr.io/actions/workflows/coredns.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/coredns.yml) |
| k8s.gcr.io/autoscaling | [k8sgcrioautoscaling](https://hub.docker.com/u/k8sgcrioautoscaling) | [![k8sgcrioautoscaling](https://github.com/x-mirrors/gcr.io/actions/workflows/autoscaling.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/autoscaling.yml) |
| k8s.gcr.io/scheduler-plugins | [k8sgcrioschedulerplugins](https://hub.docker.com/u/k8sgcrioschedulerplugins) | [![k8sgcrioschedulerplugins](https://github.com/x-mirrors/gcr.io/actions/workflows/scheduler-plugins.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8sgcrioschedulerplugins.yml) |
| k8s.gcr.io/ingress-nginx | [k8sgcrioingressnginx](https://hub.docker.com/u/k8sgcrioingressnginx) | [![k8sgcrioingressnginx](https://github.com/x-mirrors/gcr.io/actions/workflows/ingress-nginx.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/ingress-nginx.yml) |
| k8s.gcr.io/infra-tools | [k8sgcrioinfratools](https://hub.docker.com/orgs/k8sgcrioinfratools) | [![k8sgcrioinfratools](https://github.com/x-mirrors/gcr.io/actions/workflows/infra-tools.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/infra-tools.yml) |
| k8s.gcr.io/metrics-server | [k8sgcriometricsserver](https://hub.docker.com/u/k8sgcriometricsserver) | [![k8sgcriometricsserver](https://github.com/x-mirrors/gcr.io/actions/workflows/metrics-server.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/metrics-server.yml) |
| gcr.io/ml-pipeline | [gcriomlpipeline](https://hub.docker.com/u/gcriomlpipeline) | [![gcriomlpipeline](https://github.com/x-mirrors/gcr.io/actions/workflows/ml-pipeline.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/ml-pipeline.yml) |
| gcr.io/google-samples | [gcriogooglesamples](https://hub.docker.com/u/gcriogooglesamples) | [![gcriogooglesamples](https://github.com/x-mirrors/gcr.io/actions/workflows/google-samples.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/google-samples.yml) |
| gcr.io/tekton-releases/github.com/tektoncd/_f_/cmd/_n_ | [gcriotekton](https://hub.docker.com/u/gcriotekton) | [![gcriotekton](https://github.com/x-mirrors/gcr.io/actions/workflows/tekton.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/tekton.yml) |

- Quay

|  Quay.io | Docker | Status |
| ------------ | ------------ | ------------ |
| quay.io/metallb | [quayiometallb](https://hub.docker.com/u/quayiometallb) | [![quayiometallb](https://github.com/x-mirrors/gcr.io/actions/workflows/metallb.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/metallb.yml) |
| quay.io/coreos | [qcoreos](https://hub.docker.com/u/qcoreos) | [![quay.io/coreos](https://github.com/x-mirrors/gcr.io/actions/workflows/qcoreos.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/qcoreos.yml) |

- Knative

|  GCR | Docker | Status |
| ------------ | ------------ | ------------ |
| gcr.io/knative-releases/knative.dev/_f_/cmd/_n_ | [gcrioknative](https://hub.docker.com/u/gcrioknative) | [![gcrioknative](https://github.com/x-mirrors/gcr.io/actions/workflows/knative.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/knative.yml) |

replace `gcr.io/knative-releases/knative.dev/serving/cmd/activator` to `gcrioknative/serving-activator`

## sync request

- create issue in this repo
- send request to `me@xiexianbin.cn`

## generates image lists

```
# gcloud container images list --project google-containers
gcloud container images list --repository us.gcr.io/k8s-artifacts-prod | awk -F "/" '{print "k8s.gcr.io/"$3}'
gcloud container images list --repository k8s.gcr.io/scheduler-plugins
gcloud container images list --repository k8s.gcr.io/ingress-nginx
gcloud container images list --repository k8s.gcr.io/coredns
gcloud container images list --project ml-pipeline
gcloud container images list --repository k8s.gcr.io/autoscaling
gcloud container images list --repository k8s.gcr.io/metrics-server
gcloud container images list --repository gcr.io/google-samples

# knative.txt
for i in $(gcloud container images list --repository gcr.io/knative-releases/knative.dev | grep -v -i name); do gcloud container images list --repository $i/cmd; done > gcr.io/knative-releases.txt

# tekton.txt
for i in $(gcloud container images list --repository gcr.io/tekton-releases/github.com/tektoncd | grep -v -i name); do gcloud container images list --repository $i/cmd; done > tekton.txt
```

quay image from :
- https://quay.io/search?q=coreos
- https://quay.io/api/v1/repository?last_modified=true&namespace=coreos&popularity=true&public=true&quota=false

- https://github.com/kubernetes/k8s.io/blob/main/k8s.gcr.io/Vanity-Domain-Flip.md

## ref

- [old mirrors repo](https://github.com/x-mirrors/gcmirrors)
- [mirror workflow/Kubernetes gcr/quay 镜像同步和国内加速介绍](https://www.xiexianbin.cn/open-sources/google-container-registry-mirrors/)
- build your own mirrors use [python3-cisctl](https://github.com/x-actions/python3-cisctl/)
- kubernetes v1.25 容器注册服务由 k8s.gcr.io 迁移到 registry.k8s.io
