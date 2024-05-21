from sqlalchemy import Column, Integer, String, ForeignKey, Table, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, mapped_column
import datetime

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    email_address: Mapped[str] = mapped_column(String, unique=True, index=True)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")
    likes: Mapped[list["Like"]] = relationship("Like", back_populates="user")
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, default=datetime.datetime.now
    )

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    content: Mapped[str] = mapped_column(String)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    author: Mapped["User"] = relationship("User", back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")
    categories: Mapped[list["Category"]] = relationship("Category", secondary="post_category")
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary="post_tag")
    likes: Mapped[list["Like"]] = relationship("Like", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text_area: Mapped[str] = mapped_column(String)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship("Post", back_populates="comments")

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    posts: Mapped[list["Post"]] = relationship("Post", secondary="post_category")

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    posts: Mapped[list["Post"]] = relationship("Post", secondary="post_tag")

class Like(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))
    user: Mapped["User"] = relationship("User", back_populates="likes")
    post: Mapped["Post"] = relationship("Post", back_populates="likes")

post_category = Table(
    "post_category",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)

post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)
