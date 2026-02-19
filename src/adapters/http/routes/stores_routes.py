import logging
from fastapi import APIRouter, Depends, HTTPException, Path

from application.use_cases.get_store_use_case import GetStoreUseCase
from ..schemas.store_schema import StoreGetRequest
from ..dependencies.store_dependencies import get_store_use_case
from ..dependencies.auth_dependencies import get_token_header
from domain.exceptions.store_exceptions import StoreNotFoundError

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
    dependencies=[Depends(get_token_header)]
)


logger = logging.getLogger(__name__)


@router.get("/{store_id}", summary="Consulta uma loja")
def get_store(
    store_id: int = Path(..., gt=0),
    use_case: GetStoreUseCase = Depends(get_store_use_case)
):
    logger.info(f"Recebida solicitação de consulta de loja: {store_id}")
    store = use_case.execute(store_id)
    logger.info(f"Loja consultada {store_id}: {store}")
    return {"store_id": store_id, "store": store}



@router.post("/get-store", summary="Consulta uma loja")
def get_store(
    request: StoreGetRequest,
    use_case: GetStoreUseCase = Depends(get_store_use_case)
):
    store = use_case.execute(request.store_id)

    return {
        "store_id": request.store_id,
        "store": store
    }