from fastapi import APIRouter
from Fudge.service_state import afp
from .actions import read_config, save_config
from .models import AFPService, AFPSettings

router = APIRouter(
    prefix="/afp"
)


@router.get("/info", response_model=AFPService)
async def service_info():
    info = afp()
    return info


@router.get("/settings", response_model=AFPSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=AFPSettings)
async def save_settings(c: AFPSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
