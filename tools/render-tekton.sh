for i in $(gcloud container images list --repository gcr.io/tekton-releases/github.com/tektoncd | grep -v -i name); do
  gcloud container images list --repository $i/cmd | grep $i;
done > ../gcr.io/tekton-releases.txt
