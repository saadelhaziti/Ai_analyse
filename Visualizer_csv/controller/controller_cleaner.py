

from  Visualizer_csv.services.pip_line_cleaner import AutoDataCleaner
import pandas as pd
from fastapi.responses import JSONResponse
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio
from DB_Save.Models_save.Minio_forma_save import Froma_Minio
import os
#clean data and save in form csv

def clean_data(input_filename: str):
    if not input_filename.endswith('.csv'):
        return JSONResponse(status_code=400, content={"message": "Input file must be a CSV."})
    dir_path, filename = os.path.split(input_filename)
    file_stream, _ = Get_file_from_minio(input_filename)
    df = pd.read_csv(file_stream, encoding='utf-8')
    if df.empty:
        return {"message": "Input file is empty."}
    cleaner = AutoDataCleaner(df)
    cleaner.execute_pipeline()


    
    output_stream = Froma_Minio(cleaner.df)
    output_filename = dir_path + "/" + "cleaned_" + filename
    file_url = POST_file_in_Minio(output_stream, output_filename, "text/csv")
    return file_url

# 22-28


