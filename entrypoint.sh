#!/bin/sh

echo "Iniciando aplicação..."

# Aqui você pode rodar migrações, seeds, validações etc
# exemplo:
# alembic upgrade head

exec uvicorn main:app --reload --app-dir src   --host 0.0.0.0 --port 8000