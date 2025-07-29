import io
from DB_Save.controller.Minio_controller import POST_file_in_Minio

def upload_prompt_to_minio(prompt: str, filename: str = "schema_prompt.txt") -> str:
    try:
        # Convertir le prompt en flux binaire
        prompt_stream = io.BytesIO()
        prompt_stream.write(prompt.encode("utf-8"))
        prompt_stream.seek(0)

        # Upload dans MinIO
        file_url = POST_file_in_Minio(
            prompt_stream,
            filename,
            content_type="text/plain"
        )

        return file_url

    except Exception as e:
        raise Exception(f"Erreur lors de l'upload vers MinIO : {str(e)}")
