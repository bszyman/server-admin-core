from fastapi import APIRouter
from Fudge.service_state import nfs
from .actions import read_config, save_config
from .models import NFSService, NFSSettings

router = APIRouter(
    prefix="/nfs"
)


@router.get("/info", response_model=NFSService)
async def service_info():
    info = nfs()
    return info


@router.get("/settings", response_model=NFSSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=NFSSettings)
async def save_settings(c: NFSSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
