gcloud container images list --repository gcr.io/google-containers | grep -v -i name > ../gcr.io/google-containers.txt
echo "# gcloud container images list --repository gcr.io/google-containers" >> ../gcr.io/google-containers.txt
