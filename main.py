from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ⬇️ importe les ROUTERS (pas des apps)
from Visualizer_csv.routes import router as csv_router
from Visualizer_DB.routes import router as db_router
from DB_Save.routes import Save_API as save_router
from chatbot.routes import Chat as chat_router
from users.routes import Users as users_router

from chatbot.services.chatbot_services import chat_manager
from users.Models.model import Base
from users.services.database import engine

app = FastAPI(
    title="Auto Chart Generator API",
    description="API for automatic data cleaning and chart generation from CSV files.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await chat_manager.initialize()

# ⬇️ monte les routers (remplace l’ancien api_router/app1)
app.include_router(csv_router, prefix="/Visualizer_csv", tags=["Visualizer_csv"])
app.include_router(save_router, prefix="/DB_Save", tags=["DB_Save"])
app.include_router(db_router,  prefix="/Visualizer_DB", tags=["Visualizer_DB"])
app.include_router(chat_router, prefix="/chatbot", tags=["chatbot"])
app.include_router(users_router, prefix="/users", tags=["users"])

Base.metadata.create_all(bind=engine)
