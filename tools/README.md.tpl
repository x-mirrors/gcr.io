# gcr.io

利用 [Github Action](https://github.com/x-actions/python3-cisctl) 同步 Google/Quay 等容器镜像到 hub.docker.com，实现曲线加速被墙 [kubernetes](https://www.xiexianbin.cn/kubernetes) 和 [云原生](https://www.xiexianbin.cn/cloud-native) 的相关镜像问题。

已同步镜像在线查询：https://mirrors.kb.cx

## 已同步镜像

{{ mk_raw }}

使用示例，将原来的 `gcr.io/knative-releases/knative.dev/serving/cmd/activator` 替换为 `gcrioknative/serving-activator`

## 新增同步需求

发送邮件到 `me@xiexnabin.cn` 或在 https://github.com/x-mirrors/gcr.io/ 提交 `issue`

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
