from fastapi import Request, status

from src.core.http.exceptions import HttpError


class BaseController:
    def _raise(self, status_code: int, error: str, message: str):
        raise HttpError(status_code, error, message)

    def bad_request(self, message: str):
        self._raise(status.HTTP_400_BAD_REQUEST, "Bad Request", message)

    def unauthorized(self, message: str = "Acesso não autorizado."):
        self._raise(status.HTTP_401_UNAUTHORIZED, "Unauthorized", message)

    def not_found(self, message: str):
        self._raise(status.HTTP_404_NOT_FOUND, "Not Found", message)

    def forbidden(self, message: str = "Acesso negado."):
        self._raise(status.HTTP_403_FORBIDDEN, "Forbidden", message)

    def conflict(self, message: str = "Conflito de dados."):
        self._raise(status.HTTP_409_CONFLICT, "Conflict", message)

    def unprocessable_entity(self, message: str = "Entidade não processável."):
        self._raise(
            status.HTTP_422_UNPROCESSABLE_CONTENT,
            "Unprocessable Entity",
            message,
        )

    def get_current_user(self, request: Request) -> dict:
        payload = getattr(request.state, "jwt_payload", None)
        if not payload:
            self.unauthorized()
        return payload
