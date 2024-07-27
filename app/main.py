from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from app.database.schema import Base
from app.database.session import SessionLocal, engine
from app.router import router
from app.config import config


def get_settings():
    return config.Settings()


async def startup():
    Base.metadata.create_all(bind=engine)


async def shutdown():
    SessionLocal.close_all()


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()


app = FastAPI(title="Sample App", version="0.0.1", lifespan=app_lifespan)
FastAPI.include_router(app, router=router)


@app.get("/", tags=["welcome"])
def welcome(request: Request):
    return "Welcome to Sample Technology backend API Verion 1"


@app.get("/admin", tags=["welcome"])
def admin(request: Request):
    return "This page is for Admin"


@app.get("/app/{app_id}", tags=["welcome"])
def app_id(request: Request, app_id: str):
    return f"This app ID is {app_id} "


@app.get("/ping", tags=["welcome"])
def ping(request: Request):
    return "pong"
