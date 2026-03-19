from prisma import Prisma

from src.application.models.posts import CreatePostDTO, UpdatePostDTO
from src.application.services.base_service import BaseService


class PostsService(BaseService[CreatePostDTO, UpdatePostDTO, object]):
    def __init__(self, db: Prisma):
        self.db = db

    async def create(self, data: CreatePostDTO):
        return await self.db.post.create(
            data={
                "content": data.content,
                "published_at": data.published_at,
            }
        )

    async def list(self):
        return await self.db.post.find_many(
            order={"created_at": "desc"}
        )

    async def get_by_id(self, id: str):
        return await self.db.post.find_unique(where={"id": id})

    async def update(self, id: str, data: UpdatePostDTO):
        return await self.db.post.update(
            where={"id": id},
            data=data.model_dump(exclude_unset=True),
        )

    async def delete(self, id: str) -> None:
        await self.db.post.delete(where={"id": id})

    async def like(self, id: str):
        return await self.db.post.update(
            where={"id": id},
            data={"likes": {"increment": 1}},
        )
