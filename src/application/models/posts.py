from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class CreatePostDTO(BaseModel):
    content: str = Field(..., max_length=500)
    published_at: Optional[datetime] = None


class UpdatePostDTO(BaseModel):
    content: Optional[str] = Field(None, max_length=500)
    published_at: Optional[datetime] = None


class PostResponseDTO(BaseModel):
    id: str
    content: str
    likes: int
    published_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, post):
        return cls(
            id=post.id,
            content=post.content,
            likes=post.likes,
            published_at=post.published_at,
            created_at=post.created_at,
            updated_at=post.updated_at,
        )


class PostDTO:
    Create = CreatePostDTO
    Update = UpdatePostDTO
    Response = PostResponseDTO
    ListResponse = List[PostResponseDTO]
