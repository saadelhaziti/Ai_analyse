import json
from Visualizer_csv.services.Analyse_csv import analyze_and_generate_charts

def analyze_controll(csv_path: str, output_path: str = "charts.json"):
    try:
        # Call the function and get charts (must be a JSON-serializable object)
        charts = analyze_and_generate_charts(csv_path, output_path)

        # Save to file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(charts, f, indent=2, ensure_ascii=False)

        return charts  # return the Python object, not a JSONResponse

    except Exception as e:
        raise RuntimeError(f"Erreur dans analyze_controll: {str(e)}") from e
