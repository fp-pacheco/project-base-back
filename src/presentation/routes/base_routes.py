from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from fastapi import APIRouter

TController = TypeVar("TController")


class BaseRoutes(ABC, Generic[TController]):
    def __init__(self, router: APIRouter, controller: TController):
        self.router = router
        self.controller = controller
        self.register_routes()

    @abstractmethod
    def register_routes(self):
        """
        Método abstrato para registrar as rotas no router.
        Cada subclasse deve implementar este método.
        """
        pass
