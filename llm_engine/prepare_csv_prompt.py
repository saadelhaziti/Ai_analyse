import pandas as pd
import numpy as np
import json
from DB_Save.controller.Minio_controller import Get_file_from_minio

def prepare_csv_prompt_input(file_stream: str):

    # 3. Load DataFrame
    file_stream, content_type = Get_file_from_minio(file_stream)
    df = pd.read_csv(file_stream, encoding='utf-8')
    print("dataframe loaded")
    # 4. Generate metadata
    sample = df.head(5).to_string(index=False)  # Preview of first 5 rows
    columns = df.dtypes.astype(str).to_dict()   # Column names + types
    unique_counts = df.nunique().sort_values(ascending=False).to_dict()
    corr_matrix = (
        df.select_dtypes(include=[np.number])
        .corr()
        .round(2)# change precision to 2 decimal places
        .to_dict()
    )

    # 5. Package everything into a dict for prompt rendering
    return {
        "input_filename": file_stream,
        "sample": sample,
        "columns": json.dumps(columns, indent=2),
        "unique_counts": json.dumps(unique_counts, indent=2),
        "corr_matrix": json.dumps(corr_matrix, indent=2),
    }



