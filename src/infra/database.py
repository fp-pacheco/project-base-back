from contextlib import asynccontextmanager

from fastapi import FastAPI

from prisma import Prisma


class Database:
    def __init__(self):
        self.client = Prisma()

    async def connect(self):
        await self.client.connect()

    async def disconnect(self):
        await self.client.disconnect()

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        await self.connect()
        try:
            yield
        finally:
            await self.disconnect()
