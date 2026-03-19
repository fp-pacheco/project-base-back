from src.application.use_cases import UseCases
from src.presentation.controllers.health import HealthController
from src.presentation.controllers.posts import PostsController


class Controllers:
    def __init__(self, use_cases: UseCases):
        self.health = HealthController()
        self.post = PostsController(use_cases=use_cases.post)
