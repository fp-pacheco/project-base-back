from abc import ABC
from typing import Generic, TypeVar

from src.core.http.exceptions import EntityNotFoundException

TService = TypeVar("TService")


class BaseUseCases(ABC, Generic[TService]):
    def __init__(self, service: TService):
        self.service = service

    async def _ensure_entity_exists(self, id: str):
        entity = await self.service.get_by_id(id)
        if not entity:
            raise EntityNotFoundException(id)
        return entity
