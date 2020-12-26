from fastapi import APIRouter
from Fudge.service_state import application_server
from .actions import read_config, save_config
from .models import MailService, MailSettings

router = APIRouter(
    prefix="/mail"
)


@router.get("/info", response_model=MailService)
async def service_info():
    info = application_server()
    return info


@router.get("/settings", response_model=MailSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=MailSettings)
async def save_settings(c: MailSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
