import os
from google.cloud import storage


def upload_to_gcs(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client(project=os.environ.get("USER"))
    bucket = storage_client.bucket(os.environ.get("GOOGLE_CLOUD_STORAGE_BUCKET"))
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")


