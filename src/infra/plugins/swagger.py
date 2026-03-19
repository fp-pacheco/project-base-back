from fastapi.openapi.utils import get_openapi

from src.core.settings import Settings


class Swagger:
    def __init__(self, app):
        self.app = app

    def configure(self):
        def custom_openapi():
            if self.app.openapi_schema:
                return self.app.openapi_schema

            openapi_schema = get_openapi(
                title="Base API",
                version=Settings.API_VERSION,
                description="Documentação da Base API com autenticação Bearer",
                routes=self.app.routes,
            )

            openapi_schema["components"]["securitySchemes"] = {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }

            for path in openapi_schema["paths"].values():
                for method in path.values():
                    method.setdefault("security", []).append(
                        {"BearerAuth": []}
                    )

            self.app.openapi_schema = openapi_schema
            return self.app.openapi_schema

        self.app.openapi = custom_openapi
