for i in $(gcloud container images list --repository gcr.io/knative-releases/knative.dev | grep -v -i name); do
  gcloud container images list --repository $i/cmd | grep $i;
done > ../gcr.io/knative-releases.txt
