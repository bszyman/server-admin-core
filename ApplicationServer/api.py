from fastapi import APIRouter
from Fudge.service_state import application_server
from .actions import read_config, save_config
from .models import ApplicationServerService, ApplicationServerSettings

router = APIRouter(
    prefix="/application-server"
)


@router.get("/info", response_model=ApplicationServerService)
async def service_info():
    info = application_server()
    return info


@router.get("/settings", response_model=ApplicationServerSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=ApplicationServerSettings)
async def save_settings(c: ApplicationServerSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
