from pydantic import parse_file_as
from .models import XgridSettings
from config import Settings

env = Settings()
config_file_path = "{0}/xgrid.json".format(env.config_directory)


def read_config():
    settings = parse_file_as(XgridSettings, config_file_path)
    return settings


def save_config(config: XgridSettings):
    with open(config_file_path, "w") as f:
        f.write(config.json())

    settings = parse_file_as(XgridSettings, config_file_path)
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
