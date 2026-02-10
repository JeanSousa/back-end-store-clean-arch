from domain.entities.store import Store
from domain.interfaces.stores_repository_interface import IStoreRepository

class StoreMemoryRespository(IStoreRepository):
    def get_store(self, store_id: int) -> Store:
        return Store(store_id, 'Los Pollos Hermanos', '(21) 97158-3808')