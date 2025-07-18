from  Visualizer_csv.services.pip_line_cleaner import AutoDataCleaner
import io

def Froma_Minio(cleaner: AutoDataCleaner) :
    """
    Function to save data in Minio storage.
    """
    output_stream = io.BytesIO()
    cleaner.df.to_csv(output_stream, index=False)
    output_stream.seek(0)

    return output_stream