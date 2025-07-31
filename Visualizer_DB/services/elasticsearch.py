from elasticsearch import Elasticsearch
import uuid

class ElasticsearchInterface:
    def __init__(self, host="http://elasticsearch:9200", index_name="default-index"):
        self.es = Elasticsearch(hosts=[host])
        self.index = index_name

    def save(self, document: dict, doc_id=None):
        if doc_id is None:
            doc_id = str(uuid.uuid4())
        response = self.es.index(index=self.index, id=doc_id, document=document)  # ✅ Correction ici
        return response['_id']

    def retrieve(self, doc_id: str):
        if not self.es.exists(index=self.index, id=doc_id):
            return False
        response = self.es.get(index=self.index, id=doc_id)
        return response['_source']
