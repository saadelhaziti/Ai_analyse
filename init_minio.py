import os
import time
import boto3
from botocore.exceptions import ClientError

MINIO_URL = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")

def wait_for_minio():
    import requests
    print("Waiting for MinIO to be ready...")
    while True:
        try:
            r = requests.get(f"{MINIO_URL}/minio/health/live")
            if r.status_code == 200:
                print("MinIO is up!")
                return
        except:
            pass
        time.sleep(2)

def create_bucket_if_not_exists():
    s3 = boto3.client(
        "s3",
        endpoint_url=MINIO_URL,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )
    try:
        s3.head_bucket(Bucket=MINIO_BUCKET_NAME)
        print(f"Bucket '{MINIO_BUCKET_NAME}' already exists.")
    except ClientError:
        print(f"Creating bucket '{MINIO_BUCKET_NAME}'...")
        s3.create_bucket(Bucket=MINIO_BUCKET_NAME)
        print(f"Bucket '{MINIO_BUCKET_NAME}' created.")

if __name__ == "__main__":
    wait_for_minio()
    create_bucket_if_not_exists()
