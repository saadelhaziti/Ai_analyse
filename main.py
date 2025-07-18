from fastapi import FastAPI
from Visualizer_csv.routes import app as api_router
from DB_Save.routes import Save_API as save_router


app = FastAPI(title="Auto Chart Generator API",
                description="API for automatic data cleaning and chart generation from CSV files.",
                version="1.0.0"
                )


app.include_router(api_router, prefix="/Visualizer_csv", tags=["Visualizer_csv"])
app.include_router(save_router, prefix="/DB_Save", tags=["DB_Save"])