import uvicorn
from fastapi import APIRouter, FastAPI

from src.application.services import Services
from src.application.use_cases import UseCases
from src.core.settings import Settings
from src.infra.database import Database
from src.infra.middlewares.error_handling import GlobalExceptionMiddleware
from src.infra.plugins.cors import Cors
from src.infra.plugins.swagger import Swagger
from src.presentation.controllers import Controllers
from src.presentation.routes import Routes


class Server:
    def __init__(self):
        self.db = Database()
        self.app = FastAPI(
            title="Base API",
            lifespan=self.db.lifespan,
        )
        self.router = APIRouter()

        self._setup_plugins()
        self._setup_middlewares()
        self._setup_modules()

    def _setup_plugins(self):
        Cors(self.app).configure()
        Swagger(self.app).configure()

    def _setup_middlewares(self):
        self.app.add_middleware(GlobalExceptionMiddleware)

    def _setup_modules(self):
        self.services = Services(self.db.client)
        self.use_cases = UseCases(self.services)
        self.controllers = Controllers(self.use_cases)
        self.routes = Routes(self.app, self.router, self.controllers)

    def start(self):
        uvicorn.run(self.app, host=Settings.API_HOST, port=int(Settings.API_PORT))


server = Server()
app = server.app

if __name__ == "__main__":
    server.start()
