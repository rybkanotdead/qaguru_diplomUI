import os
from typing import Literal

from pydantic import BaseSettings


BASE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(BASE_DIR, '.env')

EnvType = Literal['local', 'remote']


class Settings(BaseSettings):
    ENVIRONMENT: EnvType = 'local'
    USER_LOGIN: str
    USER_PASSWORD: str
    API_PASSWORD: str
    SELENOID_LOGIN: str
    SELENOID_PASSWORD: str

    class Config:
        env_file = ENV_PATH


settings = Settings()
