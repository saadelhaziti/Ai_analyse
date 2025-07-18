from pydantic import BaseModel

class GenerateInput(BaseModel):
    prompt_path: str
    output_path: str
    model: str = 'mistral'
