class HttpError(Exception):
    def __init__(self, status_code: int, error: str, message: str):
        self.status_code = status_code
        self.error = error
        self.message = message


class CustomException(Exception):
    """Exceção base para todos os erros de domínio."""
    pass


class EntityNotFoundException(CustomException):
    def __init__(self, entity_id: str):
        self.entity_id = entity_id
        super().__init__(f"Entidade com id '{entity_id}' não encontrada.")


class EmailAlreadyExistsException(CustomException):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"O e-mail '{email}' já está em uso.")


class InvalidCredentialsException(CustomException):
    def __init__(self, reason: str = "Credenciais inválidas."):
        super().__init__(reason)


class InvalidEmailException(CustomException):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Formato de e-mail inválido: '{email}'.")


class PasswordNotSetException(CustomException):
    def __init__(self):
        super().__init__("Senha ainda não configurada.")


class AlreadyExistsException(CustomException):
    def __init__(self, field: str, value: str):
        self.field = field
        self.value = value
        super().__init__(f"Já existe um registro com {field} '{value}'.")


class AlreadyActiveException(CustomException):
    def __init__(self, entity: str, entity_id: str):
        super().__init__(f"{entity} '{entity_id}' já está ativo.")


class AlreadyInactiveException(CustomException):
    def __init__(self, entity: str, entity_id: str):
        super().__init__(f"{entity} '{entity_id}' já está inativo.")
