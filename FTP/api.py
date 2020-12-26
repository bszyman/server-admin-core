from fastapi import APIRouter
from Fudge.service_state import ftp
from .actions import read_config, save_config
from .models import FTPService, FTPSettings

router = APIRouter(
    prefix="/ftp"
)


@router.get("/info", response_model=FTPService)
async def service_info():
    info = ftp()
    return info


@router.get("/settings", response_model=FTPSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=FTPSettings)
async def save_settings(c: FTPSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
