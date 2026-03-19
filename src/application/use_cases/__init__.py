from src.application.services import Services
from src.application.use_cases.posts import PostsUseCases


class UseCases:
    def __init__(self, services: Services):
        self.post = PostsUseCases(services.post)
