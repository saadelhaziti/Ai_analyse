from fastapi import APIRouter,  UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
from DB_Save.controller.Minio_controller import POST_file_in_Minio, Get_file_from_minio
from Models.schema import DocumentModel
from DB_Save.controller.controller_elasticSearch import save_document_controller, retrieve_documents_by_project_controller
Save_API = APIRouter()



@Save_API.post("/Save_in_to_Minio")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_url = POST_file_in_Minio(file, file.filename, file.content_type)
        return {
            "message": "File uploaded successfully to MinIO.",
            "file_url": file_url,
            "filename": file.filename
        }
    except ValueError as ve:
        return JSONResponse(status_code=400, content={"message": str(ve)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Upload failed: {str(e)}"})
    


@Save_API.get("/Get_from_Minio/{filename}")
async def get_file(filename: str):
    try:
        file_stream, content_type = Get_file_from_minio(filename)
        return StreamingResponse(file_stream, media_type=content_type)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found in MinIO.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving file: {str(e)}")
    



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

