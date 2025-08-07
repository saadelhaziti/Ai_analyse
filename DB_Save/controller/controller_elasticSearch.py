from DB_Save.Models_save.ElasticSearch import ElasticsearchStorage
from fastapi.responses import JSONResponse
from fastapi import HTTPException

def save_document_controller(document: dict, index_name: str = "visualizations"):
    try:
        es = ElasticsearchStorage(index_name=index_name)
        doc_id = es.save(document)
        return {
            "message": "Document indexed successfully.",
            "document_id": doc_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error indexing document: {str(e)}")


def retrieve_documents_by_project_controller(project_name: str, index_name: str = "visualizations"):
    try:
        es = ElasticsearchStorage(index_name=index_name)
        documents = es.search_by_project(project_name)
        
        if not documents:
            raise HTTPException(status_code=404, detail=f"Aucun document trouvé pour le projet '{project_name}'.")
        
        return {"results": documents}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération : {str(e)}")
