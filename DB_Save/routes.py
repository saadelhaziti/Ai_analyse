from fastapi import APIRouter,  UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
from DB_Save.controller.Minio_controller import POST_file_in_Minio, Get_file_from_minio
from Visualizer_csv.controller.controller_cleaner import clean_data
from Models.schema import DocumentModel
from DB_Save.controller.controller_elasticSearch import save_document_controller, retrieve_documents_by_project_controller
from sqlalchemy.orm import Session
import io   
import csv
from DB_Save.Models_save.Minio import MinIOStorage
from users.Models.schemas import ProjectCreate
from users.services.database import SessionLocal
from users.controller.Project_controller import update_project_controller
from users.services.Project_Services import get_project
from Visualizer_csv.services.meta_data import meta_data
import json
Save_API = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@Save_API.post("/Save_in_to_Minio/{guid_project}")
async def upload_file(guid_project: str,file: UploadFile = File(...),db: Session = Depends(get_db)):
    try:
        proj = get_project(db, guid_project)
        cleaned_filename = (
            file.filename if file.filename.startswith("cleaned_")
            else "cleaned_" + file.filename
        )
        user_id = str(proj.guid_user)  # or username if available
        project_name = guid_project
        key_path = f"{user_id}/{project_name}/{file.filename}"
        clean_data_filename = f"{user_id}/{project_name}/{cleaned_filename}"
        file_url = POST_file_in_Minio(file, key_path, file.content_type)
        
        minio_storage = MinIOStorage()
        get_file = minio_storage.exists(clean_data_filename)
        if get_file is not True:
            response = clean_data(key_path)
            metadata = meta_data(key_path)
            update_payload = ProjectCreate(
                guid_user=str(proj.guid_user),  # You can fetch or pass the actual user if needed
                Project_name=proj.Project_name,
                data_type=proj.data_type,  # Assuming you have a data_type field in your
                data_url_clean=response,
                data_prute_url=file_url,
                metadata_url=metadata,
            )
            update_project_controller(guid_project, update_payload, db)
          # Adjust the URL as needed
        
        return {
            "message": "File uploaded successfully to MinIO.",
            "file_url": file_url,
            "filename": file.filename,
            "cleaned_data_url": response 
        }
    except ValueError as ve:
        return JSONResponse(status_code=400, content={"message": str(ve)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Upload failed: {str(e)}"})

#prepare the endpoint of csv file to jeso 
@Save_API.get("/Get_from_Minio/{filename:path}")
async def proxy_csv(filename: str):
    try:
        if filename.endswith('.json'):
            file_stream, _ = Get_file_from_minio(filename)
            result = file_stream.read().decode("utf-8")
            return json.loads(result)
        file_stream, _ = Get_file_from_minio(filename)
        # Parse CSV content into a list of dictionaries
        content = file_stream.read().decode("utf-8")

        reader = csv.DictReader(io.StringIO(content))
        json_data = []
        for row in reader:
            parsed_row = {}
            for k, v in row.items():
                v = v.strip()
                if v == "":
                    parsed_row[k] = None
                elif v.replace(".", "", 1).isdigit():
                    parsed_row[k] = float(v) if "." in v else int(v)
                else:
                    parsed_row[k] = v
            json_data.append(parsed_row)

        return JSONResponse(content=json_data)

    except e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch from MinIO: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CSV parsing failed: {e}")




@Save_API.post("/Elastic_Save")
async def save_documents(documents: list[DocumentModel]):
    indexed_ids = []
    for doc in documents:
        doc_id = save_document_controller(doc.dict())
        indexed_ids.append(doc_id)
    return {"status": "success", "indexed_ids": indexed_ids}


@Save_API.get("/Elastic_GetByProject/{project_name}")
async def get_documents_by_project(project_name: str):
    return retrieve_documents_by_project_controller(project_name)

