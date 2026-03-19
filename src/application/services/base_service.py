from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TCreate = TypeVar("TCreate")
TUpdate = TypeVar("TUpdate")
TEntity = TypeVar("TEntity")


class BaseService(ABC, Generic[TCreate, TUpdate, TEntity]):
    @abstractmethod
    async def create(self, data: TCreate) -> TEntity:
        pass

    @abstractmethod
    async def list(self) -> list[TEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> TEntity | None:
        pass

    @abstractmethod
    async def update(self, id: str, data: TUpdate) -> TEntity:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass
