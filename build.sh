docker buildx build . --platform linux/amd64 -t gcp-bindincapi
docker tag gcp-bindincapi gcr.io/playground-dennisvink/gcp-bindincapi
docker push gcr.io/playground-dennisvink/gcp-bindincapi
gcloud run deploy gcp-bindincapi --image gcr.io/playground-dennisvink/gcp-bindincapi --platform managed --region us-east1 --allow-unauthenticated --timeout=900
