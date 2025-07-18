from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Visualizer_csv.controller.controller_cleaner import clean_data
from Visualizer_csv.controller.controller_analyst import analyze_controll


app = APIRouter()


@app.get("/cleaner")
def cleaner(input_path: str):
    
    # Clean data and save in form csv
    try:
        result = clean_data(input_path)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    return JSONResponse(content={"message": result})
@app.get("/analyst")
def analyst(csv_path: str, output_path: str = "charts.json"):
    try:
        charts = analyze_controll(csv_path, output_path)
        return {"charts": charts}  # Let FastAPI handle the serialization
    except Exception as e:
        print(" Erreur interne :", str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})


