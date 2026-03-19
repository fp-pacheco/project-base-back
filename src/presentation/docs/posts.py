from src.application.models.posts import PostDTO
from src.presentation.docs.error import ERROR_RESPONSES

POST_RESPONSES = {
    200: {"model": PostDTO.Response},
    **ERROR_RESPONSES,
}

POST_LIST_RESPONSES = {
    200: {"model": PostDTO.ListResponse},
    **ERROR_RESPONSES,
}

POST_CREATE_RESPONSES = {
    201: {"model": PostDTO.Response},
    **ERROR_RESPONSES,
}

POST_UPDATE_RESPONSES = {
    200: {"model": PostDTO.Response},
    **ERROR_RESPONSES,
}
