from pydantic import parse_file_as
from .models import ChatSettings
from config import Settings

env = Settings()
config_file_path = "{0}/chat.json".format(env.config_directory)


def read_config():
    print(env.config_directory)
    settings = parse_file_as(ChatSettings, config_file_path)
    return settings


def save_config(config: ChatSettings):
    with open(config_file_path, "w") as f:
        f.write(config.json())

    settings = parse_file_as(ChatSettings, config_file_path)
    return settings


def apply_config():
    pass


def read_log():
    pass


def start_service():
    pass


def stop_service():
    pass


def restart_service():
    pass
