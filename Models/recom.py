from users.services.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from users.services.Project_Services import get_project
from DB_Save.controller.Minio_controller import POST_file_in_Minio, Get_file_from_minio
import requests
import json
import io

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
def generate_recommendation(project_guid : str, db: Session = Depends(get_db)):
    proj = get_project(db, project_guid)

    data_type = proj.data_type 

    
    if data_type == "csv":
        content_csv, _ = Get_file_from_minio(proj.metadata_url)
        content =  content_csv.read().decode('utf-8')
    elif data_type == "sql":
        schema_sql, _ = Get_file_from_minio(proj.data_url_clean)
        schema = schema_sql.read().decode('utf-8')
        metadata_sql, _ = Get_file_from_minio(proj.metadata_url)
        metadata = metadata_sql.read().decode('utf-8')
        content = f"Schema: {schema}\nMetadata: {metadata}"

    prompt_template =f"""
You are a business intelligence assistant.

Based on the following {data_type}, generate a **JSON list of useful recommendations**.
Each item must be a dictionary with a single key:
- "recommendation": a clear sentence combining the action to take AND its purpose.

Only respond with the JSON list, no additional text, explanations, or markdown code blocks (no ```).

Here is an example of a valid response:

[
  {{ "recommendation": "Analyze sales by category to identify the most profitable ones." }},
  {{ "recommendation": "Study customer reviews to improve the products." }}
]

### info:
Content: {content}
""" 

    response = requests.post(
        "http://ollama:11434/api/generate",  # Use Docker service name here
        json={"model": "mistral:7b", "prompt": prompt_template},
        stream=True
    )
    if response.status_code != 200:
        raise ValueError(f"Failed to call Ollama API: {response.text}")
    full_response_text = ""
    try:
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                # Append the 'response' part to full text
                full_response_text += data.get("response", "")
        charts = json.loads(full_response_text)
        key_path = f"{proj.guid_user}/{project_guid}/recommendation.json"
        json_data = json.dumps(charts, indent=2)
        POST_file_in_Minio(io.BytesIO(json_data.encode("utf-8")), key_path, "application/json")
        print("Recommendation generated and saved to MinIO:", charts)
    except Exception as e:
        raise ValueError(f"Error parsing response: {str(e)}") from e        