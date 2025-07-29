from fastapi import APIRouter , Depends
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from DB_Save.Models_save.Minio_forma_save import Froma_Minio
from Visualizer_DB.services.generateLLMprompt import generate_llm_prompt_from_credentials
from Models.db_credentials import DBCredentials
from Visualizer_DB.services.generationJSON import generate_json_via_llm
import os, json, io
from DB_Save.controller.Minio_controller import POST_file_in_Minio
from users.services.Project_Services import get_project
from users.services.database import SessionLocal
from users.Models.schemas import ProjectCreate
from users.controller.Project_controller import update_project_controller
from sqlalchemy.orm import Session
from Visualizer_DB.services.execute import load_visualizations_from_file
from Visualizer_DB.services.execute import execute_queries_and_store
from Visualizer_DB.services.elasticsearch import ElasticsearchInterface
from Visualizer_DB.services.meta_data import meta_data
from Visualizer_DB.controller.saveschemaMINIO import upload_prompt_to_minio

app1 = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app1.post("/connect/{guid_project}")
def connect_db(guid_project: str, credentials: DBCredentials, db: Session = Depends(get_db)):
    try:
        proj = get_project(db, guid_project)
        # 1. Générer le prompt
        prompt = generate_llm_prompt_from_credentials(credentials.dict())

        schema_path = f"{str(proj.guid_user)}/{guid_project}/schema.txt"
        metadata_path = f"{str(proj.guid_user)}/{guid_project}/metadata.txt"
        current_dir = os.path.dirname(__file__) 
        db_config_path = os.path.abspath(os.path.join(current_dir, "db_credentials.json"))
        metadata_url = meta_data(db_config_path,metadata_path)
        file_url = upload_prompt_to_minio(prompt, schema_path)
        update_payload = ProjectCreate(
                guid_user=str(proj.guid_user),  # You can fetch or pass the actual user if needed
                Project_name=proj.Project_name,
                data_type=proj.data_type,  # Assuming you have a data_type field in your
                data_url_clean=schema_path,
                data_prute_url=proj.data_prute_url,
                metadata_url=metadata_url,
            )
        update_project_controller(guid_project, update_payload, db)
        
        return {
            "message": "Prompt enregistré dans MinIO",
            "file_url": file_url, 
            "metadata": metadata_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")

@app1.get("/generate-JSON/{guid_project}")
def generate_visualizations(guid_project: str,  db: Session = Depends(get_db)):
    
    try:
        proj = get_project(db, guid_project)

        result = generate_json_via_llm(
            schema_txt_path=proj.data_url_clean,
            user_value=guid_project
        )
        dir_path, _ = os.path.split(proj.data_url_clean)
        current_dir = os.path.dirname(__file__)  
        db_config_path = os.path.abspath(os.path.join(current_dir, "db_credentials.json"))
        results = execute_queries_and_store(result, db_config_path, dir_path,guid_project)
        # 2. Préparation indexation Elasticsearch
        es = ElasticsearchInterface(index_name="visualizations")
        indexed_ids  = []

        for viz in results:
            doc_id = es.save(viz)
            indexed_ids.append(doc_id)

        return {
            "status": "success"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
