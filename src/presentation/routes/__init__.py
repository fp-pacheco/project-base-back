from fastapi import APIRouter, FastAPI

from src.presentation.controllers import Controllers
from src.presentation.routes.health import HealthRoute
from src.presentation.routes.posts import PostsRoute


class Routes:
    def __init__(self, app: FastAPI, router: APIRouter, controllers: Controllers):
        self.app = app
        self.router = router
        self.controllers = controllers
        self.register_routes()
        self.include_router()

    def register_routes(self):
        self.health = HealthRoute(self.router, self.controllers.health)
        self.post = PostsRoute(self.router, self.controllers.post)

    def include_router(self):
        self.app.include_router(self.router)
