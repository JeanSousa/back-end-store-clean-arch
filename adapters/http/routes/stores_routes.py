import logging
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


logger = logging.getLogger(__name__)
store_repo = StoreMemoryRespository()

@router.get("/{store_id}", summary="Consulta uma loja")
def get_store(store_id: int):
    logger.info(f"Recebida solicitação de consulta de loja: {store_id}")
    use_case = GetStoreUseCase(store_repo)
    try:
        store = use_case.execute(store_id)
        logger.info(f"Loja consultada {store_id}: {store}")
        return {"store_id": store_id, "store": store}
    except Exception as e:
        logger.error(f"Erro ao consultar loja pelo id {store_id}: {e}", exc_info=True)
        raise HTTPException(status_code=404, detail=str(e))
