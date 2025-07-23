from fastapi import FastAPI
from Visualizer_csv.routes import app as api_router
from DB_Save.routes import Save_API as save_router
from users.routes import Users as Users_router
from users.Models.model import Base
from users.services.database import engine
from Visualizer_DB.routes import app1 as api_router1
app = FastAPI(title="Auto Chart Generator API",
                description="API for automatic data cleaning and chart generation from CSV files.",
                version="1.0.0"
                )


app.include_router(api_router, prefix="/Visualizer_csv", tags=["Visualizer_csv"])
app.include_router(save_router, prefix="/DB_Save", tags=["DB_Save"])

app.include_router(api_router1, prefix="/Visualizer_DB", tags=["Visualizer_DB"])


Base.metadata.create_all(bind=engine)

app.include_router(Users_router, prefix="/users", tags=["users"])
