import logging
import traceback

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.http.exceptions import HttpError

logger = logging.getLogger(__name__)


class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    """Middleware global para capturar exceções e retornar JSON padronizado."""

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)

        except (ValidationError, RequestValidationError) as exc:
            return JSONResponse(
                status_code=422,
                content={
                    "error": "Erro de validação",
                    "details": exc.errors(),
                },
            )

        except HttpError as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "error": exc.error,
                    "message": exc.message,
                },
            )

        except Exception as exc:
            if "UniqueViolationError" in type(exc).__name__:
                return JSONResponse(
                    status_code=409,
                    content={
                        "error": "Conflict",
                        "message": "Já existe um registro com estes dados.",
                    },
                )

            logger.error(f"Erro inesperado: {exc}\n{traceback.format_exc()}")

            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "message": "Ocorreu um erro inesperado.",
                },
            )
