from fastapi import FastAPI, HTTPException
from application.use_cases.get_store import GetStoreUseCase
from infrastructure.repositories.stores_repository import StoreMemoryRespository
from infrastructure.logging.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Cadastro de lojas", version="1.0.0")

store_repo = StoreMemoryRespository()


@app.get("/stores/{store_id}", summary="Consulta uma loja")
def get_store(store_id: int):
    logger.info(f"Recebida solicitação de consulta de loja: {store_id}")
    use_case = GetStoreUseCase(store_repo)
    try:
        store = use_case.execute(store_id)
        logger.info(f"Loja consultada {store_id}: {store}")
        return {"store_id": store_id, "saldo": store}
    except Exception as e:
        logger.error(f"Erro ao consultar loja pelo id {store_id}: {e}", exc_info=True)
        raise HTTPException(status_code=404, detail=str(e))

