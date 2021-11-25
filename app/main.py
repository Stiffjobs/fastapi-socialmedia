from fastapi import FastAPI
from . import models
from .database import engine
from app.routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import SQLALCHEMY_DATABASE_URL

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": {
            # "my value": f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}",
            # "correct_value": SQLALCHEMY_DATABASE_URL
            "hello world I'm stiffjobs!",
        }
    }
