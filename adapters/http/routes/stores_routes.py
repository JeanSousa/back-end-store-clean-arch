from fastapi import APIRouter, Depends, HTTPException
from application.use_cases.get_store import GetStoreUseCase
from infrastructure.repositories.stores_repository import StoreMemoryRespository

from ..dependencies.stores_dependencies import get_token_header

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}}
)


store_repo = StoreMemoryRespository()

@router.get("/{store_id}", summary="Consulta uma loja")
def get_store(store_id: int):
    use_case = GetStoreUseCase(store_repo)
    try:
        store = use_case.execute(store_id)
        return {"store_id": store_id, "store": store}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
