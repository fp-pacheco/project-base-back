from prisma import Prisma

from src.application.services.posts import PostsService


class Services:
    def __init__(self, db: Prisma):
        self.post = PostsService(db)
