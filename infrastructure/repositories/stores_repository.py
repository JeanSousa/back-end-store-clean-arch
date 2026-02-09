from domain.entities.store import Store
from domain.interfaces.stores_repository_interface import IStore

class StoreMemoryRespository(IStore):
    def get_store(self, store_id: int) -> Store:
        return Store(store_id, 'Los Pollos Hermanos', '(21) 97158-3808')