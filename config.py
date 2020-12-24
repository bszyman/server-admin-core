from pydantic import BaseSettings


class Settings(BaseSettings):
    config_directory: str = "/var/local/sa-core"

    class Config:
        env_file = ".env"
