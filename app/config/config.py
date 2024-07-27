from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from typing import List
import base64


# load_dotenv(f"{os.path.dirname(__file__)}/.env")
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # SECRET_KEY: str = os.environ.get("SECRET_KEY")
    # ALGORITHIM: str = os.environ.get("ALGORITHIM")
    # # access_token
    # ACCESS_TOKEN_EXPIRE_MINS: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINS")
    # ACCESS_SECRET_KEY: str = os.environ.get("ACCESS_SECRET_KEY")

    # # refresh_token
    # REFRESH_TOKEN_EXPIRE_MINS: int = os.environ.get("REFRESH_TOKEN_EXPIRE_MINS")
    # REFRESH_SECRET_KEY: str = os.environ.get("REFRESH_SECRET_KEY")
    # TOKEN_WRAPPER_KEY: str = os.environ.get("TOKEN_WRAPPER_KEY")
    # TOKEN_WRAPPER_SALT: str = os.environ.get("TOKEN_WRAPPER_SALT")

    # # password token
    # RESET_PASSWORD_SECRET_KEY: str = os.environ.get("RESET_PASSWORD_SECRET_KEY")
    # RESET_PASSWORD_SALT: str = os.environ.get("RESET_PASSWORD_SALT")

    # postgres database
    POSTGRESS_PASSWORD: str = os.environ.get("POSTGRESS_PASSWORD")
    POSTGRESS_USER: str = os.environ.get("POSTGRESS_HOST")

    # Mongo Database
    MONGO_INITDB_ROOT_USERNAME: str = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
    MONGO_INITDB_ROOT_PASSWORD: str = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

    # # Fastap- mail
    # MAIL_USERNAME: str = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD")
    # MAIL_FROM: str = os.environ.get("MAIL_FROM")
    # MAIL_PORT: int = os.environ.get("MAIL_PORT")
    # MAIL_SERVER: str = os.environ.get("MAIL_SERVER")
    # MAIL_STARTTLS: bool = os.environ.get("MAIL_STARTTLS")
    # MAIL_SSL_TLS: bool = os.environ.get("MAIL_SSL_TLS")
    # USE_CREDENTIALS: bool = os.environ.get("USE_CREDENTIALS")
    # VALIDATE_CERTS: bool = os.environ.get("VALIDATE_CERTS")

    # # redis db
    # REDIS_BACKEND: str = os.environ.get("REDIS_BACKEND")

    # # HCP Frontend Host
    # HCP_FRONTEND_HOST_PORTAL_URL: str = os.environ.get("HCP_FRONTEND_HOST_PORTAL_URL")

    # # Service_user Frontend Host
    # FRONTEND_HOST_LOGIN_URL: str = os.environ.get("FRONTEND_HOST_LOGIN_URL")
    # FRONTEND_HOST_RESET_PASSWORD_URL: str = os.environ.get(
    #     "FRONTEND_HOST_RESET_PASSWORD_URL"
    # )

    # # contact
    # BACKEND_DEV_EMAIL: str = os.environ.get("BACKEND_DEV_EMAIL")

    # # ipconfig
    # IPCONFIG_KEY: str = os.environ.get("IPCONFIG_KEY")

    # # cloudiary
    # CLOUDINARY_CLOUD_NAME: str = os.environ.get("CLOUDINARY_CLOUD_NAME")
    # CLOUDINARY_API_KEY: str = os.environ.get("CLOUDINARY_API_KEY")
    # CLOUDINARY_API_SECRET: str = os.environ.get("CLOUDINARY_API_SECRET")
