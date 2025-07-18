from  Visualizer_csv.services.pip_line_cleaner import AutoDataCleaner
import pandas as pd
from fastapi.responses import JSONResponse
from Models.Interface import StorageInterface
from DB_Save.controller.Minio_controller import POST_file_in_Minio, Get_file_from_minio
from DB_Save.Models_save.Minio_forma_save import Froma_Minio
#clean data and save in form csv

def clean_data(input_filename: str):
    if not input_filename.endswith('.csv'):
        return JSONResponse(status_code=400, content={"message": "Input file must be a CSV."})

    file_stream, content_type = Get_file_from_minio(input_filename)
    df = pd.read_csv(file_stream, encoding='utf-8')

    if df.empty:
        return JSONResponse(status_code=400, content={"message": "Input file is empty."})

    cleaner = AutoDataCleaner(df)
    cleaner.execute_pipeline()

    output_stream = Froma_Minio(cleaner)

    output_filename = "cleaned_" + input_filename

    file_url = POST_file_in_Minio(output_stream, output_filename, "text/csv")

    return f"Data cleaned and saved to {output_filename} at {file_url}"

# 22-28
