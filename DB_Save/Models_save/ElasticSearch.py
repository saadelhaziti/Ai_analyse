from Models.abstract import StorageBackend
from elasticsearch import Elasticsearch
import uuid

class ElasticsearchStorage(StorageBackend):
    def __init__(self, host="http://localhost:9200", index_name="default-index"):
        self.es = Elasticsearch(hosts=[host])
        self.index = index_name

    def save(self, document: dict, doc_id=None):
        if doc_id is None:
            doc_id = str(uuid.uuid4())
        response = self.es.index(index=self.index, id=doc_id, document=document)  # ✅ Correction ici
        return response['_id']

    def retrieve(self, doc_id: str):
        if not self.es.exists(index=self.index, id=doc_id):
            return None
        response = self.es.get(index=self.index, id=doc_id)
        return response['_source']
    def search_by_project(self, project_name: str):
        query = {
            "query": {
                "match": {
                    "projet": project_name
                }
            }
        }
        try:
            result = self.es.search(index=self.index, body=query)
            return [hit["_source"] for hit in result["hits"]["hits"]]
        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")
            return []










# # Elasticsearch Implementation
# from Models.abstract import StorageBackend
# from elasticsearch import Elasticsearch, helpers

# class ElasticsearchStorage(StorageBackend):
#     def __init__(self, es_host: str, index_name: str):
#         self.index_name = index_name
#         self.es = Elasticsearch(es_host)

#         if not self.es.ping():
#             raise Exception("❌ Elasticsearch ne répond pas.")

#     def save(self, key: str, data: list[dict]) -> None:
#         actions = [
#             {
#                 "_index": self.index_name,
#                 "_source": {
#                     "id_visualisation": doc.get("id_visualisation"),
#                     "titre": doc.get("titre"),
#                     "data": doc.get("data")
#                 }
#             }
#             for doc in data
#         ]

#         if actions:
#             helpers.bulk(self.es, actions)
#             print(f"✅ {len(actions)} documents sauvegardés dans Elasticsearch (index: {self.index_name})")
#         else:
#             print("⚠️ Aucun document à sauvegarder.")

#     def retrieve(self, key: str) -> dict:
#         try:
#             res = self.es.get(index=self.index_name, id=key)
#             return res["_source"]
#         except Exception as e:
#             print(f"❌ Erreur lors de la récupération : {e}")
#             return {}
