import json
from Visualizer_csv.services.Analyse_csv import analyze_and_generate_charts

def analyze_controll(csv_path: str):
    try:
        # Call the function and get charts (must be a JSON-serializable object)
        charts = analyze_and_generate_charts(csv_path)
        if not charts:
            raise ValueError("No charts generated from the analysis.")
        return charts  # return the Python object, not a JSONResponse

    except Exception as e:
        raise RuntimeError(f"Erreur dans analyze_controll: {str(e)}") from e
