from fastapi import FastAPI
from fastapi.responses import JSONResponse
from infrastructure.logging.logging_config import setup_logging
from adapters.http.routes import stores_routes
from domain.exceptions.store_exceptions import StoreNotFoundError

setup_logging()

app = FastAPI(title="Cadastro de lojas", version="1.0.0")

app.include_router(stores_routes)

@app.exception_handler(StoreNotFoundError)
async def store_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )