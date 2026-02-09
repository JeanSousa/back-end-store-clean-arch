from domain.interfaces.stores_repository_interface import IStore
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

class GetStoreUseCase:
    def __init__(self, repository: IStore):
        self.repository = repository

    def execute(self, store_id: int):
        store = self.repository.get_store(store_id)
        if is_null_or_empty(store):
            raise Exception('Loja não encontrada')
        else:
            return store 
        

