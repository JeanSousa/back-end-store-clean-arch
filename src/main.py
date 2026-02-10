from fastapi import FastAPI
from infrastructure.logging.logging_config import setup_logging
from adapters.http.routes import stores_routes

setup_logging()

app = FastAPI(title="Cadastro de lojas", version="1.0.0")

app.include_router(stores_routes)

