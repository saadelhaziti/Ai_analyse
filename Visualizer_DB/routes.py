from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from DB_Save.Models_save.Minio_forma_save import Froma_Minio
from Visualizer_DB.services.generateLLMprompt import generate_llm_prompt_from_credentials
from Visualizer_DB.services.credentails import DBCredentials
from Visualizer_DB.services.generationJSON import generate_json_via_llm
import os, json, io
from DB_Save.controller.Minio_controller import POST_file_in_Minio

app1 = APIRouter()


@app1.post("/connect")
def connect_db(credentials: DBCredentials):
    try:
        # 1. Générer le prompt à partir des credentials
        prompt = generate_llm_prompt_from_credentials(credentials.dict())

        # 2. Convertir le prompt en BytesIO
        prompt_stream = io.BytesIO()
        prompt_stream.write(prompt.encode("utf-8"))
        prompt_stream.seek(0)

        # 3. Définir un nom de fichier
        prompt_filename = "schema_prompt.txt"

        # 4. Upload vers MinIO
        file_url = POST_file_in_Minio(
            prompt_stream,
            prompt_filename,
            content_type="text/plain"
        )

        return {
            "message": "Prompt enregistré dans MinIO",
            "file_url": file_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")


@app1.get("/generate-JSON")
def generate_visualizations():
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY", "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")
    
    try:
        result = generate_json_via_llm(
            schema_txt_path="./schema.txt",
            output_json_path="./outputschema.json",
            openrouter_api_key=openrouter_api_key,
            user_value="project"
        )
        return {
            "status": "success",
            "message": "Visualisations générées avec succès",
            "results": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }