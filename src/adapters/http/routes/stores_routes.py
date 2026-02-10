import logging
from fastapi import APIRouter, Depends, HTTPException

from application.use_cases.get_store_use_case import GetStoreUseCase
from ..schemas.store_schema import StoreGetRequest
from ..dependencies.store_dependencies import get_store_use_case
from ..dependencies.auth_dependencies import get_token_header

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
    dependencies=[Depends(get_token_header)]
)


logger = logging.getLogger(__name__)


@router.get("/{store_id}", summary="Consulta uma loja")
def get_store(
    request: StoreGetRequest = Depends(),
    use_case: GetStoreUseCase = Depends(get_store_use_case)
):
    logger.info(f"Recebida solicitação de consulta de loja: {request.store_id}")
    try:
        store = use_case.execute(request.store_id)
        logger.info(f"Loja consultada {request.store_id}: {store}")
        return {"store_id": request.store_id, "store": store}
    except Exception as e:
        logger.error(f"Erro ao consultar loja pelo id {request.store_id}: {e}", exc_info=True)
        raise HTTPException(status_code=404, detail=str(e))
