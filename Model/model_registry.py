import json
import os
from google.cloud import storage

def push_model_metadata_to_registry(model_name, performance_metrics, bucket_name='your-bucket-name'):
    model_metadata = {
        "model_name": model_name,
        "performance": performance_metrics,
        "model_version": "v1",
        "timestamp": "2025-03-23"
    }
    metadata_filename = f"{model_name}_metadata.json"
    with open(metadata_filename, 'w') as f:
        json.dump(model_metadata, f)
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"model_metadata/{metadata_filename}")
    blob.upload_from_filename(metadata_filename)
    print(f"Metadata for {model_name} uploaded to {bucket_name}/model_metadata/{metadata_filename}")
    os.remove(metadata_filename)
