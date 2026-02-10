from domain.entities.store import Store
from domain.interfaces.stores_repository_interface import IStoreRepository
from application.use_cases.get_store_use_case import GetStoreUseCase
import pytest


class FakeStoreRepository(IStoreRepository):
    def __init__(self):
        self.stores = {
            1: Store(1, "Los Pollos Hermanos", "(21) 99999-9999")
        }

    def get_store(self, store_id: int):
        return self.stores.get(store_id)


def test_should_return_store_when_store_exists():
    repo = FakeStoreRepository()
    use_case = GetStoreUseCase(repo)

    store = use_case.execute(1)

    assert store.name == "Los Pollos Hermanos"


def test_should_raise_exception_when_store_not_found():
    repo = FakeStoreRepository()
    use_case = GetStoreUseCase(repo)

    with pytest.raises(Exception):
        use_case.execute(999)