# Project Base — Backend

Projeto base para APIs REST em Python. Estruturado para ser reaproveitado como ponto de partida em qualquer novo projeto, com arquitetura limpa, autenticação JWT e integração com banco via Prisma.

---

## Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web
- **[Prisma](https://prisma-client-py.readthedocs.io/)** — ORM com suporte a PostgreSQL
- **[Pydantic](https://docs.pydantic.dev/)** — validação de dados
- **[PyJWT](https://pyjwt.readthedocs.io/)** — autenticação JWT
- **[bcrypt](https://pypi.org/project/bcrypt/)** — hash de senhas
- **[Uvicorn](https://www.uvicorn.org/)** — servidor ASGI
- **[pytest](https://docs.pytest.org/)** — testes

---

## Arquitetura

O projeto segue os princípios de **Clean Architecture**, organizado em quatro camadas com responsabilidades bem definidas:

```
src/
├── core/               # Transversal: configurações e exceções
│   ├── settings.py
│   └── http/
│       └── exceptions.py
│
├── infra/              # Detalhes técnicos: banco, auth, plugins
│   ├── database.py
│   ├── auth/
│   │   ├── token.py
│   │   ├── payload.py
│   │   └── decorators.py
│   ├── security/
│   │   └── password.py
│   ├── middlewares/
│   │   └── error_handling.py
│   └── plugins/
│       ├── cors.py
│       └── swagger.py
│
├── application/        # Regras de negócio
│   ├── models/         # DTOs de entrada e saída (Pydantic)
│   ├── services/       # Acesso ao banco via Prisma
│   └── use_cases/      # Orquestração e regras de domínio
│
└── presentation/       # Interface HTTP
    ├── controllers/    # Tratamento de request/response e erros HTTP
    ├── routes/         # Definição de endpoints
    └── docs/           # Schemas de resposta para o Swagger
```

### Fluxo de uma requisição

```
Route → Controller → UseCases → Service → Prisma (DB)
```

| Camada | Responsabilidade |
|---|---|
| **Route** | Define path, método HTTP, status codes e docs |
| **Controller** | Recebe request, chama use case, trata exceções com `try/except` |
| **UseCases** | Regras de negócio, validações e lançamento de exceções de domínio |
| **Service** | Exclusivamente operações de banco via Prisma |

---

## Configuração

### Pré-requisitos

- Python 3.11+
- PostgreSQL

### Instalação

```bash
# Clone o repositório
git clone <repo-url>
cd project-base-back

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Variáveis de ambiente

Copie o arquivo de exemplo e preencha os valores:

```bash
cp .env.example .env
```

| Variável | Descrição |
|---|---|
| `APP_ENV` | Ambiente da aplicação (`dev`, `prod`) |
| `API_HOST` | Host do servidor (ex: `0.0.0.0`) |
| `API_PORT` | Porta do servidor (ex: `8000`) |
| `API_VERSION` | Versão da API (ex: `1.0.0`) |
| `JWT_SECRET_KEY` | Chave secreta para assinar tokens JWT |
| `DATABASE_URL` | String de conexão PostgreSQL |

### Banco de dados

```bash
# Gere o client Prisma
prisma generate

# Execute as migrations
prisma migrate dev
```

### Rodando o servidor

```bash
python main.py
```

A documentação interativa (Swagger) estará disponível em `http://localhost:{API_PORT}/docs`.

---

## Como usar como base para um novo projeto

1. Clone ou copie este repositório
2. Renomeie o projeto no `main.py` (`title` do FastAPI) e no `swagger.py`
3. Remova o módulo de exemplo (`posts`) de todas as camadas
4. Adicione o model do seu domínio no `prisma/schema.prisma` e rode `prisma migrate dev`
5. Crie os arquivos do novo módulo seguindo a estrutura:

```
application/models/<modulo>.py    # DTOs
application/services/<modulo>.py  # herda BaseService
application/use_cases/<modulo>.py # herda BaseUseCases
presentation/controllers/<modulo>.py
presentation/routes/<modulo>.py
presentation/docs/<modulo>.py
```

6. Registre o módulo nos `__init__.py` de cada camada

---

## Autenticação

O projeto inclui um sistema JWT funcional com:

- `@auth_required` — valida o token e injeta o payload em `request.state.jwt_payload`
- `@require_roles(["role"])` — valida se o usuário tem a role necessária na empresa ativa
- `get_current_user(request)` — helper no `BaseController` para acessar o payload

```python
@auth_required
@require_roles(["admin"])
async def meu_endpoint(self, request: Request):
    user = self.get_current_user(request)
```

### Hash de senhas

```python
from src.infra.security.password import hash, verify

hashed = hash("minha_senha")
ok = verify("minha_senha", hashed)
```

---

## Testes

```bash
pytest
pytest --cov=src  # com cobertura
```

---

## Docker

```bash
docker compose up
```

> Configure as variáveis de ambiente no `.env` ou diretamente no `docker-compose.yml` antes de subir.

---

## Exceções disponíveis

Todas em `src/core/http/exceptions.py`:

| Exceção | Uso |
|---|---|
| `EntityNotFoundException` | Entidade não encontrada por ID |
| `EmailAlreadyExistsException` | E-mail duplicado |
| `InvalidCredentialsException` | Credenciais inválidas no login |
| `InvalidEmailException` | Formato de e-mail inválido |
| `PasswordNotSetException` | Senha ainda não configurada |
| `AlreadyExistsException` | Registro duplicado genérico |
| `AlreadyActiveException` | Entidade já está ativa |
| `AlreadyInactiveException` | Entidade já está inativa |
