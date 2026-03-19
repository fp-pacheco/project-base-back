from src.application.models.posts import CreatePostDTO, UpdatePostDTO
from src.application.use_cases.posts import PostsUseCases
from src.core.http.exceptions import EntityNotFoundException
from src.presentation.controllers.base_controller import BaseController


class PostsController(BaseController):
    def __init__(self, use_cases: PostsUseCases):
        self.use_cases = use_cases

    async def create(self, data: CreatePostDTO):
        return await self.use_cases.create(data)

    async def list_all(self):
        return await self.use_cases.list_all()

    async def get_by_id(self, post_id: str):
        try:
            return await self.use_cases.get_by_id(post_id)
        except EntityNotFoundException:
            self.not_found(f"Post '{post_id}' não encontrado.")

    async def update(self, post_id: str, data: UpdatePostDTO):
        try:
            return await self.use_cases.update(post_id, data)
        except EntityNotFoundException:
            self.not_found(f"Post '{post_id}' não encontrado.")

    async def delete(self, post_id: str):
        try:
            await self.use_cases.delete(post_id)
        except EntityNotFoundException:
            self.not_found(f"Post '{post_id}' não encontrado.")

    async def like(self, post_id: str):
        try:
            return await self.use_cases.like(post_id)
        except EntityNotFoundException:
            self.not_found(f"Post '{post_id}' não encontrado.")
