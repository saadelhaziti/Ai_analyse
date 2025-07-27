from  Visualizer_csv.services.pip_line_cleaner import AutoDataCleaner
import io
import pandas as pd

def Froma_Minio(df: pd.DataFrame) -> io.BytesIO:
    """
    Function to save data in Minio storage.
    """
    output_stream = io.BytesIO()
    df.to_csv(output_stream, index=False)
    output_stream.seek(0)

    return output_stream