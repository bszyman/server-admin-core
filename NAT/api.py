from fastapi import APIRouter
from Fudge.service_state import nat
from .actions import read_config, save_config
from .models import NATService, NATSettings

router = APIRouter(
    prefix="/nat"
)


@router.get("/info", response_model=NATService)
async def service_info():
    info = nat()
    return info


@router.get("/settings", response_model=NATSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=NATSettings)
async def save_settings(c: NATSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
