gcloud functions deploy function_name --runtime=python310 --memory 128MB \
 --trigger-topic topic_name

gcloud pubsub topics publish topic_name \
  --message="start function seller_crypto_bot"

gcloud scheduler jobs create pubsub job_name \
    --location=us-central1 \
    --schedule '0 * * * *' \
    --time-zone  "America/Sao_Paulo" \
    --topic topic_name \
    --message-body "Start Function"