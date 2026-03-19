from fastapi import APIRouter

from src.presentation.controllers.health import HealthController
from src.presentation.routes.base_routes import BaseRoutes


class HealthRoute(BaseRoutes[HealthController]):
    def __init__(self, router: APIRouter, controller: HealthController):
        super().__init__(router, controller)

    def register_routes(self):
        self.router.get(
            path="/health",
            summary="Health Check",
            tags=["Health"],
        )(self.controller.check)
