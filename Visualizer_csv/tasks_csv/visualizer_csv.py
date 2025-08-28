# tasks_csv.py
from celery_app import celery_app
from Visualizer_csv.services.pip_line_cleaner import AutoDataCleaner
from Visualizer_csv.services.execution_sql import run_queries_to_minio
from Visualizer_csv.services.meta_data import meta_data
from Visualizer_csv.services.Analyse_csv import analyze_and_generate_charts
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio
import pandas as pd

@celery_app.task
def clean_csv_task(input_path: str):
    file_stream, _ = Get_file_from_minio(input_path)
    df = pd.read_csv(file_stream, encoding="utf-8")
    cleaner = AutoDataCleaner(df)
    cleaned_df = cleaner.execute_pipeline()
    
    # sauvegarder le CSV nettoyé
    cleaned_path = input_path.replace(".csv", "_clean.csv")
    POST_file_in_Minio(cleaned_df.to_csv(index=False), cleaned_path, "text/csv")
    return {"message": f"Cleaned CSV saved at {cleaned_path}"}

@celery_app.task
def analyze_csv_task(csv_path: str, project_guid: str = None):
    charts = analyze_and_generate_charts(csv_path)
    results = run_queries_to_minio(csv_path, charts, project_guid)
    meta_file = meta_data(csv_path)
    return {"charts": results, "metadata": meta_file}
