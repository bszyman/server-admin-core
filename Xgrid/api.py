from fastapi import APIRouter
from Fudge.service_state import open_directory
from .actions import read_config, save_config
from .models import XgridService, XgridSettings

router = APIRouter(
    prefix="/xgrid"
)


@router.get("/info", response_model=XgridService)
async def service_info():
    info = open_directory()
    return info


@router.get("/settings", response_model=XgridSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=XgridSettings)
async def save_settings(c: XgridSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
