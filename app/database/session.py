# import motor.motor_asyncio
from psycopg2 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from pymongo import MongoClient
from bson import json_util
from app.config import config
from pymongo.errors import ConnectionFailure

# from .logger import logger
# from src.core.config import Settings
from sqlalchemy.exc import DataError, IntegrityError, InternalError

# redis connector
# r_connector = redis.from_url(Settings().REDIS_BACKEND)


# engine = create_engine("sqlite:///herts1.db", connect_args={"check_same_thread": False})


# engine = create_engine(
#     "postgresql+psycopg2://postgres:123456@172.20.0.4:5432/postgres",
#     echo=True,
#     echo_pool=True,
# )

engine = create_engine(
    f"postgresql+psycopg2://{config.Settings().POSTGRESS_USER}:{config.Settings().POSTGRESS_PASSWORD}@10.0.0.4:5432/postgres",
    echo=True,
    echo_pool=True,
)

SessionLocal = sessionmaker(engine)


# database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except DataError as exec:
        db.rollback()
        # logger.error(exec)
        raise HTTPException(status_code=400, detail="invalid datatype")
    except IntegrityError as exec:
        db.rollback()
        # logger.error(exec)
        raise HTTPException(
            status_code=400, detail="database fields incompatable or incomplete"
        )
    except InternalError as exec:
        db.rollback()
        # logger.error(exec)
        raise HTTPException(status_code=400, detail="incorrect datatype")

    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# pymongo

# connection_string = dbMongo.MONGO_URI
connection_string = f"mongodb://{config.Settings().MONGO_INITDB_ROOT_USERNAME}:{config.Settings().MONGO_INITDB_ROOT_PASSWORD}@10.0.0.2:27017"
# client = MongoClient(dbMongo.MONGO_URI)
# mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
db_client = MongoClient(connection_string)
try:
    db_client.admin.command("ping")
except ConnectionError as e:
    raise e
json_option = json_util.JSONOptions(json_mode=json_util.JSONMode.RELAXED)


def get_mongo_client():
    try:
        yield db_client
    finally:
        db_client.close()


mongo_client = Annotated[MongoClient, Depends(get_mongo_client)]
