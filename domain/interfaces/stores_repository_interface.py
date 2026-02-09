from abc import ABC, abstractmethod

class IStore(ABC):
    @abstractmethod
    def get_store(self, store_id: int):
        pass 



