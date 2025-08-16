# MinIO Implementation
from Models.abstract import StorageBackend
import boto3
from botocore.client import Config
import pandas as pd
import io
from fastapi import UploadFile
from DB_Save.Models_save.minio_config import (
    MINIO_ENDPOINT,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY,
    MINIO_BUCKET_NAME,
    MINIO_SECURE
)

class MinIOStorage(StorageBackend):
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            endpoint_url=MINIO_ENDPOINT,
            aws_access_key_id=MINIO_ACCESS_KEY,
            aws_secret_access_key=MINIO_SECRET_KEY,
            config=Config(signature_version="s3v4"),
            region_name="us-east-1",
        )

    def save(self, key: str, data: UploadFile) -> str:
        """
        Enregistre un fichier dans MinIO et retourne l'URL publique.
        `key` est ici le nom du fichier.
        `data` est un UploadFile (FastAPI).
        """
        try:
            if hasattr(data, 'file'):
                file_obj = data.file
                content_type = getattr(data, 'content_type', 'application/octet-stream')
            else:
            # Assume data is a file-like object (BytesIO, etc.)
                file_obj = data
                content_type = 'text/csv'  # or make this configurable

            self.s3.upload_fileobj(
                file_obj,
                MINIO_BUCKET_NAME,
                key,
                ExtraArgs={"ContentType": content_type},
            )
            # file_url = f"http{'s' if MINIO_SECURE else ''}://{MINIO_ENDPOINT}/{MINIO_BUCKET_NAME}/{key}"
            return key
        except Exception as e:
            raise RuntimeError(f"Erreur d'upload vers MinIO : {str(e)}")
        
    def retrieve(self, key: str, as_dataframe: bool = False):
        """
        Récupère un fichier depuis MinIO.
        Si as_dataframe=True et que le fichier est un CSV, retourne un DataFrame pandas.
        Sinon retourne le contenu binaire.
        """
        try:
            response = self.s3.get_object(Bucket=MINIO_BUCKET_NAME, Key=key)
            binary_data = response['Body'].read()

            if as_dataframe:
                return pd.read_csv(io.BytesIO(binary_data), encoding='utf-8')

            return binary_data

        except Exception as e:
            raise RuntimeError(f"Erreur lors de la récupération depuis MinIO : {str(e)}")
    def exists(self, key: str) -> bool:
        """
        Vérifie si un fichier existe dans MinIO (bucket/key).
        Retourne True si le fichier est trouvé, sinon False.
        """
        try:
            self.s3.head_object(Bucket=MINIO_BUCKET_NAME, Key=key)
            return True
        except self.s3.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                return False
            raise RuntimeError(f"Erreur lors de la vérification de l'existence du fichier : {str(e)}")