#!/bin/bash
set -x
export http_proxy="http://127.0.0.1:8001"; export HTTP_PROXY="http://127.0.0.1:8001"; export https_proxy="http://127.0.0.1:8001"; export HTTPS_PROXY="http://127.0.0.1:8001"
for i in $(gcloud container images list --repository gcr.io/cf-build-service-public | grep -v -i name); do
  gcloud container images list --repository $i | grep $i;
done > ../gcr.io/cf-build-service-public.txt
