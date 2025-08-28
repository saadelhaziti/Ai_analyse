from celery_app import celery_app
from Visualizer_DB.services.generateLLMprompt import generate_llm_prompt_from_credentials
from Visualizer_DB.controller.saveschemaMINIO import upload_prompt_to_minio
from Visualizer_DB.services.meta_data import meta_data
from users.controller.Project_controller import update_project_controller
from users.services.database import SessionLocal
from users.services.Project_Services import get_project
from users.Models.schemas import ProjectCreate
from Visualizer_DB.services.generationJSON import generate_json_via_llm
from Visualizer_DB.services.execute import execute_queries_and_store
from Visualizer_DB.services.elasticsearch import ElasticsearchInterface
from Models.recom import generate_recommendation
import os

@celery_app.task(name="tasks.visualizer_tasks.connect_db_task")
def connect_db_task(guid_project: str, credentials_dict: dict):
    db = SessionLocal()
    try:
        proj = get_project(db, guid_project)
        prompt = generate_llm_prompt_from_credentials(credentials_dict)

        schema_path = f"{str(proj.guid_user)}/{guid_project}/schema.txt"
        metadata_path = f"{str(proj.guid_user)}/{guid_project}/metadata.txt"
        current_dir = os.path.dirname(__file__)
        db_config_path = os.path.abspath(
            os.path.join(current_dir, "../Visualizer_DB/services/db_credentials.json")
        )

        file_url = upload_prompt_to_minio(prompt, schema_path)
        metadata_urls = meta_data(db_config_path, metadata_path, file_url)

        update_payload = ProjectCreate(
            guid_user=str(proj.guid_user),
            Project_name=proj.Project_name,
            data_type=proj.data_type,
            data_url_clean=schema_path,
            data_prute_url=proj.data_prute_url,
            metadata_url=metadata_urls,
        )
        update_project_controller(guid_project, update_payload, db)

        return {"file_url": file_url, "metadata": metadata_urls}

    except Exception as e:
        return {"error": str(e)}
    finally:
        db.close()


@celery_app.task(name="tasks.visualizer_tasks.generate_visualizations_task")
def generate_visualizations_task(guid_project: str):
    db = SessionLocal()
    try:
        proj = get_project(db, guid_project)

        result = generate_json_via_llm(
            schema_txt_path=proj.data_url_clean,
            user_value=guid_project
        )
        dir_path, _ = os.path.split(proj.data_url_clean)
        current_dir = os.path.dirname(__file__)
        db_config_path = os.path.abspath(
            os.path.join(current_dir, "../Visualizer_DB/services/db_credentials.json")
        )

        results = execute_queries_and_store(result, db_config_path, dir_path, guid_project)
        
        es = ElasticsearchInterface(index_name="visualizations")
        for viz in results:
            es.save(viz)

        generate_recommendation(guid_project, db)

        return results

    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        db.close()
