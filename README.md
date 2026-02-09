# back-end-store-clean-arch
Project example for Clean Arch

Structure:

```
.
├── adapters/                         # Camada de Interface Adapters (entrada/saída)
│   └── http/                         # Interface HTTP (FastAPI)
│       ├── dependencies/             # Dependências do FastAPI (DI, auth, composition)
│       │   ├── auth_dependencies.py  # Dependências de autenticação (headers, token, etc.)
│       │   └── store_dependencies.py # Composition root: cria use cases e injeta repositórios
│       ├── routes/                   # Definição das rotas HTTP
│       │   ├── __init__.py           # Permite importação do módulo de rotas
│       │   └── stores_routes.py      # Endpoints relacionados a lojas (Stores)
│       └── schemas/                  # Schemas Pydantic (DTOs de entrada/saída)
│           └── store_schema.py       # Validação e serialização HTTP para Store
│
├── application/                      # Camada de Application (casos de uso)
│   └── use_cases/                    # Implementação dos casos de uso
│       └── get_store_use_case.py     # Caso de uso para consulta de loja
│
├── domain/                           # Camada de Domínio (regras de negócio)
│   ├── entities/                     # Entidades de domínio
│   │   └── store.py                 # Entidade Store (modelo de negócio)
│   └── interfaces/                  # Interfaces (ports) do domínio
│       └── stores_repository_interface.py
│                                     # Contrato do repositório de Store
│
├── infrastructure/                   # Camada de Infraestrutura (detalhes técnicos)
│   ├── logging/                      # Configuração de logging da aplicação
│   │   └── logging_config.py         # Setup de logs (format, handlers, levels)
│   └── repositories/                # Implementações concretas dos repositórios
│       └── store_repository.py       # Repositório de Store (ex: memória, DB, etc.)
│
├── main.py                           # Ponto de entrada da aplicação FastAPI
├── README.md                         # Documentação do projeto
├── requirements.txt                  # Dependências do projeto
└── tests/                            # Testes unitários e de integração

```