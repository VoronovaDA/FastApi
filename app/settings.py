""" settings """
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """ settings class """
    main_url: str


settings = Settings(main_url="/")
