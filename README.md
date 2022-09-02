# gcr.io

利用 [Github Action](https://github.com/x-actions/python3-cisctl) 同步 Google/Quay 等容器镜像到 hub.docker.com，实现曲线加速被墙 [kubernetes](https://www.xiexianbin.cn/kubernetes) 和[云原生](https://www.xiexianbin.cn/cloud-native) 的相关镜像问题。

已同步进行在线查询地址：https://mirrors.kb.cx

## Which Images Syncing

使用示例，将原来的 `gcr.io/knative-releases/knative.dev/serving/cmd/activator` 替换为 `gcrioknative/serving-activator`

### gcr.io

|  GCR | Docker | Status |
| ------------ | ------------ | ------------ |
| gcr.io/distroless | [gcriodistroless](https://hub.docker.com/u/gcriodistroless) | [![gcriodistroless](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-distroless.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-distroless.yml) |
| gcr.io/google-samples | [gcriogooglesamples](https://hub.docker.com/u/gcriogooglesamples) | [![gcriogooglesamples](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-google-samples.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-google-samples.yml) |
| gcr.io/kaniko-project | [gcriokaniko](https://hub.docker.com/u/gcriokaniko) | [![gcriokaniko](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kaniko-project.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kaniko-project.yml) |
| gcr.io/knative-releases/knative.dev/_f_/cmd/_n_ | [gcrioknative](https://hub.docker.com/u/gcrioknative) | [![gcrioknative](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-knative-releases.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io--releasesknative.yml) |
| gcr.io/ml-pipeline | [gcriomlpipeline](https://hub.docker.com/u/gcriomlpipeline) | [![gcriomlpipeline](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-ml-pipeline.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-ml-pipeline.yml) |
| gcr.io/tekton-releases/github.com/tektoncd/_f_/cmd/_n_ | [gcriotekton](https://hub.docker.com/u/gcriotekton) | [![gcriotekton](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-tekton-releases.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-tekton-releases.yml) |

### k8s.gcr.io

|  GCR | Docker | Status |
| ------------ | ------------ | ------------ |
| k8s.gcr.io/autoscaling | [k8sgcrioautoscaling](https://hub.docker.com/u/k8sgcrioautoscaling) | [![k8sgcrioautoscaling](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-autoscaling.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-autoscaling.yml) |
| k8s.gcr.io/coredns | [gcmirrors](https://hub.docker.com/u/gcmirrors) | [![coredns](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-coredns.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-coredns.yml) |
| k8s.gcr.io/infra-tools | [k8sgcrioinfratools](https://hub.docker.com/orgs/k8sgcrioinfratools) | [![k8sgcrioinfratools](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-infra-tools.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-infra-tools.yml) |
| k8s.gcr.io/ingress-nginx | [k8sgcrioingressnginx](https://hub.docker.com/u/k8sgcrioingressnginx) | [![k8sgcrioingressnginx](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-ingress-nginx.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-ingress-nginx.yml) |
| k8s.gcr.io | [gcmirrors](https://hub.docker.com/u/gcmirrors) | [![k8s](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-k8s.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-k8s.yml) |
| gcr.io/metrics-server | [k8sgcriometricsserver](https://hub.docker.com/u/k8sgcriometricsserver) | [![k8sgcriometricsserver](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-metrics-server.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-metrics-server.yml) |
| k8s.gcr.io/metrics-server | [k8sgcriometricsserver](https://hub.docker.com/u/k8sgcriometricsserver) | [![k8sgcriometricsserver](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-metrics-server.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-metrics-server.yml) |
| k8s.gcr.io/scheduler-plugins | [k8sgcrioschedulerplugins](https://hub.docker.com/u/k8sgcrioschedulerplugins) | [![k8sgcrioschedulerplugins](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-scheduler-plugins.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-k8sgcrioschedulerplugins.yml) |

### quay.io

|  Quay.io | Docker | Status |
| ------------ | ------------ | ------------ |
| quay.io/argoproj | [qargoproj](https://hub.docker.com/u/qargoproj) | [![quay.io/argoproj](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-argoproj.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-argoproj.yml) |
| quay.io/ceph | [qceph](https://hub.docker.com/u/qceph) | [![quay.io/ceph](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-ceph.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-ceph.yml) |
| quay.io/coreos | [qcoreos](https://hub.docker.com/u/qcoreos) | [![quay.io/coreos](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-coreos.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-coreos.yml) |
| quay.io/metallb | [quayiometallb](https://hub.docker.com/u/quayiometallb) | [![quayiometallb](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-metallb.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-metallb.yml) |

## 新增同步需求

发送邮件到 `me@xiexnabin.cn` 或在 https://github.com/x-mirrors/gcr.io/ 提交 `issue`

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
gcloud container images list --repository gcr.io/distroless > gcr.io/distroless.txt

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
