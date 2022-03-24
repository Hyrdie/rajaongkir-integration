import os

from pydantic import BaseSettings
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME")
    APP_URL: str = os.getenv("APP_URL")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    KEY: str = os.getenv("KEY")

settings = Settings()
