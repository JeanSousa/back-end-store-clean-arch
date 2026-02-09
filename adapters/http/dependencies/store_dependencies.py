from application.use_cases.get_store_use_case import GetStoreUseCase
from infrastructure.repositories.store_repository import StoreMemoryRespository

def get_store_use_case() -> GetStoreUseCase:
    repository = StoreMemoryRespository()
    return GetStoreUseCase(repository)