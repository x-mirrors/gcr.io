# gcr.io

利用 [Github Action](https://github.com/x-actions/python3-cisctl) 同步 Google/Quay 等容器镜像到 hub.docker.com，实现曲线加速被墙 [kubernetes](https://www.xiexianbin.cn/kubernetes) 和 [云原生](https://www.xiexianbin.cn/cloud-native) 的相关镜像问题。

已同步镜像在线查询：https://mirrors.kb.cx

## 已同步镜像

|Source|Target(docker)|Sync Account|Sync Period|Image Count|Status|
|:---|:---|:---|:---|:---|:---|
|gcr.io/cloud-builders|[gcriocloudbuilders](https://hub.docker.com/u/gcriocloudbuilders)|xaction|`* 0 * * *`|29|[![gcriocloudbuilders](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-cloud-builders.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-cloud-builders.yml)|
|gcr.io/cloudsql-docker|[gcriocloudsqldocker](https://hub.docker.com/u/gcriocloudsqldocker)|xactions|`* 0 * * *`|3|[![gcriocloudsqldocker](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-cloudsql-docker.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-cloudsql-docker.yml)|
|gcr.io/distroless|[gcriodistroless](https://hub.docker.com/u/gcriodistroless)|xactions|`* 2 * * *`|45|[![gcriodistroless](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-distroless.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-distroless.yml)|
|gcr.io/google-samples|[gcriogooglesamples](https://hub.docker.com/u/gcriogooglesamples)|xiexianbin|`* 0 * * *`|117|[![gcriogooglesamples](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-google-samples.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-google-samples.yml)|
|gcr.io/heptio-images|[gcrioheptioimages](https://hub.docker.com/u/gcrioheptioimages)|xmirrors|`* 16 * * *`|55|[![gcrioheptioimages](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-heptio-images.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-heptio-images.yml)|
|gcr.io/kaniko-project|[gcriokaniko](https://hub.docker.com/u/gcriokaniko)|xmirrors|`* 2 * * *`|4|[![gcriokaniko](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kaniko-project.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kaniko-project.yml)|
|gcr.io/knative-releases|[gcrioknative](https://hub.docker.com/u/gcrioknative)|xmirrors|`* 4 * * *`|96|[![gcrioknative](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-knative-releases.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-knative-releases.yml)|
|gcr.io/kubebuilder|[kubebuilder](https://hub.docker.com/u/kubebuilder)|xactions|`* 6 * * *`|25|[![kubebuilder](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kubebuilder.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kubebuilder.yml)|
|gcr.io/kubeflow-images-public|[kubeflowimagespublic](https://hub.docker.com/u/kubeflowimagespublic)|xactions|`* 10 * * *`|133|[![kubeflowimagespublic](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kubeflow-images-public.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-kubeflow-images-public.yml)|
|gcr.io/ml-pipeline|[gcriomlpipeline](https://hub.docker.com/u/gcriomlpipeline)|xiexianbin|`* 6 * * *`|63|[![gcriomlpipeline](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-ml-pipeline.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-ml-pipeline.yml)|
|gcr.io/tekton-releases|[gcriotekton](https://hub.docker.com/u/gcriotekton)|xmirrors|`* 8 * * *`|39|[![gcriotekton](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-tekton-releases.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-tekton-releases.yml)|
|gcr.io/tfx-oss-public|[gcriotfxosspublic](https://hub.docker.com/u/gcriotfxosspublic)|xactions|`* 4 * * *`|10|[![gcriotfxosspublic](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-tfx-oss-public.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/gcr.io-tfx-oss-public.yml)|
|k8s.gcr.io/autoscaling|[k8sgcrioautoscaling](https://hub.docker.com/u/k8sgcrioautoscaling)|xmirrors|`* 14 * * *`|27|[![k8sgcrioautoscaling](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-autoscaling.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-autoscaling.yml)|
|k8s.gcr.io/coredns|[gcmirrors](https://hub.docker.com/u/gcmirrors)|xiexianbin|`* 2 * * *`|1|[![gcmirrors](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-coredns.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-coredns.yml)|
|k8s.gcr.io/infra-tools|[k8sgcrioinfratools](https://hub.docker.com/u/k8sgcrioinfratools)|xiexianbin|`* 16 * * *`|2|[![k8sgcrioinfratools](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-infra-tools.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-infra-tools.yml)|
|k8s.gcr.io/ingress-nginx|[k8sgcrioingressnginx](https://hub.docker.com/u/k8sgcrioingressnginx)|xiexianbin|`* 6 * * *`|11|[![k8sgcrioingressnginx](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-ingress-nginx.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-ingress-nginx.yml)|
|k8s.gcr.io/k8s|[gcmirrors](https://hub.docker.com/u/gcmirrors)|xianbinxie|`* */8 * * *`|518|[![gcmirrors](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-k8s.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-k8s.yml)|
|k8s.gcr.io/kustomize|[k8sgcriokustomize](https://hub.docker.com/u/k8sgcriokustomize)|xaction|`* 2 * * *`|1|[![k8sgcriokustomize](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-kustomize.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-kustomize.yml)|
|k8s.gcr.io/metrics-server|[k8sgcriometricsserver](https://hub.docker.com/u/k8sgcriometricsserver)|xmirrors|`* 12 * * *`|6|[![k8sgcriometricsserver](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-metrics-server.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-metrics-server.yml)|
|k8s.gcr.io/scheduler-plugins|[k8sgcrioschedulerplugins](https://hub.docker.com/u/k8sgcrioschedulerplugins)|xiexianbin|`* 14 * * *`|2|[![k8sgcrioschedulerplugins](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-scheduler-plugins.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-scheduler-plugins.yml)|
|k8s.gcr.io/sig-storage|[k8sgcriosigstorage](https://hub.docker.com/u/k8sgcriosigstorage)|xmirrors|`* 6 * * *`|20|[![k8sgcriosigstorage](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-sig-storage.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/k8s.gcr.io-sig-storage.yml)|
|quay.io/argoproj|[quayioargoproj](https://hub.docker.com/u/quayioargoproj)|xmirrors|`* 10 * * *`|15|[![quayioargoproj](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-argoproj.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-argoproj.yml)|
|quay.io/ceph|[quayioceph](https://hub.docker.com/u/quayioceph)|xiexianbin|`* 18 * * *`|11|[![quayioceph](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-ceph.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-ceph.yml)|
|quay.io/coreos|[qcoreos](https://hub.docker.com/u/qcoreos)|xiexianbin|`* 10 * * *`|4|[![qcoreos](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-coreos.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-coreos.yml)|
|quay.io/metallb|[quayiometallb](https://hub.docker.com/u/quayiometallb)|xiexianbin|`* 10 * * *`|2|[![quayiometallb](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-metallb.yml/badge.svg)](https://github.com/x-mirrors/gcr.io/actions/workflows/quay.io-metallb.yml)|

使用示例，将原来的 `gcr.io/knative-releases/knative.dev/serving/cmd/activator` 替换为 `gcrioknative/serving-activator`

## 新增同步需求

发送邮件到 `me@xiexianbin.cn` 或在 https://github.com/x-mirrors/gcr.io/ 提交 `issue`

## generates image lists

### gcr images

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

# knative
cd tools; sh render-knative.sh

# tekton
cd tools; sh render-tekton.sh
```

### quay images

- https://quay.io/search?q=coreos
- https://quay.io/api/v1/repository?last_modified=true&namespace=coreos&popularity=true&public=true&quota=false
- https://github.com/kubernetes/k8s.io/blob/main/k8s.gcr.io/Vanity-Domain-Flip.md

## ref

- [gcmirrors](https://github.com/x-mirrors/gcmirrors)
- [mirror workflow/Kubernetes gcr/quay 镜像同步和国内加速介绍](https://www.xiexianbin.cn/open-sources/google-container-registry-mirrors/)
- build your own mirrors use [python3-cisctl](https://github.com/x-actions/python3-cisctl/)
- kubernetes v1.25 容器注册服务由 k8s.gcr.io 迁移到 registry.k8s.io