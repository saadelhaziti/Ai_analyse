# Interface de gestion
from DB_Save.Models_save.Minio import MinIOStorage
from DB_Save.Models_save.ElasticSearch import ElasticsearchStorage
class StorageInterface:
    def __init__(self, backend_type: str):
        if backend_type == 'minio':
            self.backend = MinIOStorage()
        elif backend_type == 'elasticsearch':
            self.backend = ElasticsearchStorage()
        else:
            raise ValueError("Type de backend non supporté")

    def save(self, key: str, data: dict):
        return self.backend.save(key, data)

    def retrieve(self, key: str) -> dict:
        return self.backend.retrieve(key)