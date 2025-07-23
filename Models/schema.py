from pydantic import BaseModel
from typing import List

class DocumentModel(BaseModel):
    id: int
    title: str
    columns: List[str]
    description: str
    request_sql: str
    suggested_chart: str
    projet: str

