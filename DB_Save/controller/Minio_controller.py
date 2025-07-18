from Models.Interface import StorageInterface
import io

def POST_file_in_Minio(file_data, filename: str, content_type: str):

    storage = StorageInterface(backend_type="minio")


    if hasattr(file_data, 'file'):  # likely UploadFile
        data_to_save = file_data.file
    else:
        data_to_save = file_data  # e.g., BytesIO

    file_url = storage.save(key=filename, data=data_to_save)

    return file_url




def Get_file_from_minio(filename: str):
    storage = StorageInterface(backend_type="minio")

    # Retrieve file content as binary
    binary_data = storage.retrieve(filename)
    if not binary_data:
        raise FileNotFoundError("File not found.")

    # Create a stream and return with generic content-type
    return io.BytesIO(binary_data), "application/octet-stream"