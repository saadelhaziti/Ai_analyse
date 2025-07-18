from pydantic import BaseModel

class CleanerRequest(BaseModel):
    input_path: str
    output_path: str