from pydantic import BaseModel

class DBCredentials(BaseModel):
    dbname: str
    user: str
    password: str
    host: str
    port: int = 5432
