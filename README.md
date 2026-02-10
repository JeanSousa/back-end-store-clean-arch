# back-end-store-clean-arch
Project example for Clean Arch

### 🧠 Architeture

- **Domain**: regras de negócio puras e independentes de frameworks
- **Application**: casos de uso que orquestram o domínio
- **Adapters**: interface com o mundo externo (HTTP/FastAPI)
- **Infrastructure**: detalhes técnicos como banco de dados, logging e repositórios

### Structure:

```
.
├── src/                              # Raiz do código-fonte (importável)
│   ├── adapters/                     # Camada de Interface Adapters (entrada/saída)
│   │   └── http/                     # Interface HTTP (FastAPI)
│   │       ├── dependencies/         # Dependências do FastAPI (DI, auth, composition)
│   │       │   ├── auth_dependencies.py
│   │       │   └── store_dependencies.py
│   │       ├── routes/               # Definição das rotas HTTP
│   │       │   ├── __init__.py
│   │       │   └── stores_routes.py
│   │       └── schemas/              # Schemas Pydantic (DTOs HTTP)
│   │           └── store_schema.py
│   │
│   ├── application/                  # Camada de Application (casos de uso)
│   │   └── use_cases/
│   │       └── get_store_use_case.py
│   │
│   ├── domain/                       # Camada de Domínio (regras de negócio)
│   │   ├── entities/
│   │   │   └── store.py
│   │   └── interfaces/
│   │       └── stores_repository_interface.py
│   │
│   ├── infrastructure/               # Camada de Infraestrutura
│   │   ├── logging/
│   │   │   └── logging_config.py
│   │   └── repositories/
│   │       └── store_repository.py
│   │
│   ├── main.py                       # Ponto de entrada FastAPI
│   └── __init__.py                   # Marca src como package
│
├── tests/                            # Testes unitários e integração
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── pyproject.toml (opcional, recomendado)

```

### How to run the project:

Create venv:

```
python -m venv venv

# or your python version in linux

python3 -m venv venv 

```

Activate venv:

```
# windows:

.\venv\Scripts\activate.bat.

# linux 

 source venv/bin/activate   

```

Install dependencies with pip:

```
pip install -r requirements.txt

```

Run the project with uvicorn (not unicorn! LOL)

```
uvicorn main:app --reload --app-dir src  

```

This way you can access the Swagger documentation and test it

[Swagger](http://127.0.0.1:8000/docs)