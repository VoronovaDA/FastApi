""" settings """
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """ settings class """
    MAIN_URL: str


settings = Settings(MAIN_URL="/")
