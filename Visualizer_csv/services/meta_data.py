from DB_Save.controller.Minio_controller import POST_file_in_Minio, Get_file_from_minio
import pandas as pd
import numpy as np
import io, os
def meta_data(input_filename: str):
    """
    This function is a placeholder for any metadata-related operations.
    It can be expanded to include functionality such as retrieving metadata
    from files, databases, or other sources.
    """
    dir_path, filename = os.path.split(input_filename)
    file_stream, _ = Get_file_from_minio(input_filename)
    df = pd.read_csv(file_stream, encoding='utf-8')
    if df.empty:
        return {"message": "Input file is empty."}
    
    # Here you can implement any metadata extraction logic
    sample = df.head(5).to_string(index=False)  # Preview of first 5 rows
    columns = df.dtypes.astype(str).to_dict()   # Column names + types
    unique_counts = df.nunique().sort_values(ascending=False).to_dict()
    corr_matrix = (
        df.select_dtypes(include=[np.number])
        .corr()
        .round(2)# change precision to 2 decimal places
        .to_dict()
    )
    metadata = (
        "Sample of data:\n" + sample + "\n\n" +
        "Columns:\n" + str(columns) + "\n\n" +
        "Unique counts:\n" + str(unique_counts) + "\n\n" +
        "Correlation matrix:\n" + str(corr_matrix)
    )
    # save metadata to MinIO
    metadata_filename = f"{dir_path}/metadata_{filename.replace('.csv', '.txt')}"
    metadata_stream = io.BytesIO(metadata.encode('utf-8'))
    metadata_stream.seek(0)
    file_url = POST_file_in_Minio(metadata_stream, metadata_filename, "text/plain")
    return file_url
