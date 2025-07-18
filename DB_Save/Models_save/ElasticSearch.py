# Elasticsearch Implementation
from Models.abstract import StorageBackend
from elasticsearch import Elasticsearch, helpers

class ElasticsearchStorage(StorageBackend):
    def __init__(self, es_host: str, index_name: str):
        self.index_name = index_name
        self.es = Elasticsearch(es_host)

        if not self.es.ping():
            raise Exception("❌ Elasticsearch ne répond pas.")

    def save(self, key: str, data: list[dict]) -> None:
        actions = [
            {
                "_index": self.index_name,
                "_source": {
                    "id_visualisation": doc.get("id_visualisation"),
                    "titre": doc.get("titre"),
                    "data": doc.get("data")
                }
            }
            for doc in data
        ]

        if actions:
            helpers.bulk(self.es, actions)
            print(f"✅ {len(actions)} documents sauvegardés dans Elasticsearch (index: {self.index_name})")
        else:
            print("⚠️ Aucun document à sauvegarder.")

    def retrieve(self, key: str) -> dict:
        try:
            res = self.es.get(index=self.index_name, id=key)
            return res["_source"]
        except Exception as e:
            print(f"❌ Erreur lors de la récupération : {e}")
            return {}
