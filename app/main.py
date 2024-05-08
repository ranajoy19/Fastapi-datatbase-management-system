from fastapi import FastAPI
from views import router as views_router
from database import Base, engine

app = FastAPI()

app.include_router(views_router)

Base.metadata.create_all(bind=engine)
