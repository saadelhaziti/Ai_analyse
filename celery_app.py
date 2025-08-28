from celery import Celery
import os

celery_app = Celery(
    "Ai_analyse",
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0"),
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    imports=[
        "Visualizer_csv.tasks_csv.visualizer_csv",
        "Visualizer_DB.tasks_DB.visualizer_DB",
    ],
)
