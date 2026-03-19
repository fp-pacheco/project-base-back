from functools import wraps

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer

from src.infra.auth.token import decode

security = HTTPBearer(auto_error=False)


def _get_request(*args, **kwargs) -> Request:
    request = next(
        (arg for arg in args if isinstance(arg, Request)),
        kwargs.get("request"),
    )
    if not request:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Request não encontrado.",
        )
    return request


def _get_company_id(request: Request, **kwargs) -> str | None:
    return kwargs.get("company_id") or request.path_params.get("company_id")


def auth_required(func):
    """Valida o token JWT e injeta o payload em request.state.jwt_payload."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = _get_request(*args, **kwargs)

        credentials = await security(request)
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autenticação não fornecido.",
            )

        payload = decode(credentials.credentials)

        company_id = _get_company_id(
            request, **{k: v for k, v in kwargs.items() if k != "request"}
        )
        if company_id and company_id not in payload.get("companies", []):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você não tem acesso a esta empresa.",
            )

        request.state.jwt_payload = payload
        return await func(*args, **kwargs)

    return wrapper


def require_roles(allowed_roles: list[str]):
    """
    Valida se o usuário tem uma das roles permitidas na empresa ativa.
    Deve ser usado após @auth_required.

    Exemplo:
        @auth_required
        @require_roles(["owner", "manager"])
        async def create_employee(...):
            ...
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = _get_request(*args, **kwargs)

            payload = getattr(request.state, "jwt_payload", None)
            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Usuário não autenticado.",
                )

            company_id = _get_company_id(
                request, **{k: v for k, v in kwargs.items() if k != "request"}
            )
            if not company_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="company_id é obrigatório.",
                )

            user_roles = [
                r["role_name"]
                for r in payload.get("roles", [])
                if r.get("company_id") == company_id
            ]
            if not any(role in allowed_roles for role in user_roles):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Você não tem permissão para esta ação.",
                )

            return await func(*args, **kwargs)

        return wrapper

    return decorator
