from typing import List

from src.application.models.posts import (
    CreatePostDTO,
    PostDTO,
    PostResponseDTO,
    UpdatePostDTO,
)
from src.application.services.posts import PostsService
from src.application.use_cases.base_use_cases import BaseUseCases


class PostsUseCases(BaseUseCases[PostsService]):
    async def create(self, data: CreatePostDTO) -> PostResponseDTO:
        post = await self.service.create(data)
        return PostDTO.Response.from_entity(post)

    async def list_all(self) -> List[PostResponseDTO]:
        posts = await self.service.list()
        return [PostDTO.Response.from_entity(p) for p in posts]

    async def get_by_id(self, post_id: str) -> PostResponseDTO:
        post = await self._ensure_entity_exists(post_id)
        return PostDTO.Response.from_entity(post)

    async def update(self, post_id: str, data: UpdatePostDTO) -> PostResponseDTO:
        await self._ensure_entity_exists(post_id)
        post = await self.service.update(post_id, data)
        return PostDTO.Response.from_entity(post)

    async def delete(self, post_id: str) -> None:
        await self._ensure_entity_exists(post_id)
        await self.service.delete(post_id)

    async def like(self, post_id: str) -> PostResponseDTO:
        await self._ensure_entity_exists(post_id)
        post = await self.service.like(post_id)
        return PostDTO.Response.from_entity(post)
