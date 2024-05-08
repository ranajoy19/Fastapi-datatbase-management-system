from sqlalchemy.orm import sessionmaker
from models import   User, Post, Comment, Category, Tag, Like
from database import engine,SessionLocal

def add_dummy_users():
    Session = sessionmaker(bind=engine)
    session = Session()

    users = [
        User(name="Alice", email="alice@example.com"),
        User(name="Bob", email="bob@example.com"),
        User(name="Charlie", email="charlie@example.com"),
    ]

    session.add_all(users)
    session.commit()
    session.close()


def add_dummy_posts():
    Session = sessionmaker(bind=engine)
    session = Session()

    posts = [
        Post(title="First Post", content="Content of first post", author_id=1),
        Post(title="Second Post", content="Content of second post", author_id=2),
        Post(title="Third Post", content="Content of third post", author_id=3),
    ]

    session.add_all(posts)
    session.commit()
    session.close()


add_dummy_users()
add_dummy_posts()
