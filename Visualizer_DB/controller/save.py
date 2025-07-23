from modeles.Interface import StorageInterface
from fastapi import UploadFile
import io

def handle_file_upload(file_data, filename: str, content_type: str):
    # if not file_data:
    #     raise ValueError("No file provided.")
    # if not filename.endswith('.csv'):
    #     raise ValueError("Only CSV files are supported.")

    storage = StorageInterface(backend_type="minio")

    # Pass the file_data directly if it's a file-like object (BytesIO),
    # else if UploadFile, pass file_data.file
    if hasattr(file_data, 'file'):  # likely UploadFile
        data_to_save = file_data.file
    else:
        data_to_save = file_data  # e.g., BytesIO

    file_url = storage.save(key=filename, data=data_to_save)

    return file_url




def retrieve_file_from_minio(filename: str):
    storage = StorageInterface(backend_type="minio")

    # Retrieve file content as binary
    binary_data = storage.retrieve(filename)
    if not binary_data:
        raise FileNotFoundError("File not found.")

    # Create a stream and return with generic content-type
    return io.BytesIO(binary_data), "application/octet-stream"