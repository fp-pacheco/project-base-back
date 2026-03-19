from fastapi import APIRouter

from src.application.models.posts import PostDTO
from src.presentation.docs.posts import (
    POST_CREATE_RESPONSES,
    POST_LIST_RESPONSES,
    POST_RESPONSES,
    POST_UPDATE_RESPONSES,
)
from src.presentation.controllers.posts import PostsController
from src.presentation.routes.base_routes import BaseRoutes


class PostsRoute(BaseRoutes[PostsController]):
    def __init__(self, router: APIRouter, controller: PostsController):
        super().__init__(router, controller)

    def register_routes(self):
        self.router.get(
            path="/posts",
            summary="Listar posts",
            tags=["Posts"],
            response_model=PostDTO.ListResponse,
            responses=POST_LIST_RESPONSES,
        )(self.controller.list_all)

        self.router.post(
            path="/posts",
            summary="Criar post",
            tags=["Posts"],
            response_model=PostDTO.Response,
            status_code=201,
            responses=POST_CREATE_RESPONSES,
        )(self.controller.create)

        self.router.get(
            path="/posts/{post_id}",
            summary="Buscar post por ID",
            tags=["Posts"],
            response_model=PostDTO.Response,
            responses=POST_RESPONSES,
        )(self.controller.get_by_id)

        self.router.put(
            path="/posts/{post_id}",
            summary="Atualizar post",
            tags=["Posts"],
            response_model=PostDTO.Response,
            responses=POST_UPDATE_RESPONSES,
        )(self.controller.update)

        self.router.delete(
            path="/posts/{post_id}",
            summary="Deletar post",
            tags=["Posts"],
            status_code=204,
            responses=POST_RESPONSES,
        )(self.controller.delete)

        self.router.patch(
            path="/posts/{post_id}/like",
            summary="Curtir post",
            tags=["Posts"],
            response_model=PostDTO.Response,
            responses=POST_RESPONSES,
        )(self.controller.like)
