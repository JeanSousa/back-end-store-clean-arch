from abc import ABC, abstractmethod

class IStoreRepository(ABC):
    @abstractmethod
    def get_store(self, store_id: int):
        pass 



