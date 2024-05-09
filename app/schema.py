from pydantic import BaseModel
from typing import List
from datetime import datetime


# Pydantic schema for the User model
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True

# Pydantic schema for the Post model
class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author: UserSchema
    comments: List["CommentSchema"] = []
    categories: List["CategorySchema"] = []
    tags: List["TagSchema"] = []
    likes: List["LikeSchema"] = []

    class Config:
        orm_mode = True

# Pydantic schema for the Comment model
class CommentSchema(BaseModel):
    id: int
    text: str
    post: PostSchema

    class Config:
        orm_mode = True

# Pydantic schema for the Category model
class CategorySchema(BaseModel):
    id: int
    name: str
    posts: List[PostSchema] = []

    class Config:
        orm_mode = True

# Pydantic schema for the Tag model
class TagSchema(BaseModel):
    id: int
    name: str
    posts: List[PostSchema] = []

    class Config:
        orm_mode = True

# Pydantic schema for the Like model
class LikeSchema(BaseModel):
    id: int
    user: UserSchema
    post: PostSchema

    class Config:
        orm_mode = True
