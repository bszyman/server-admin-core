from fastapi import APIRouter
from Fudge.service_state import web_objects
from .actions import read_config, save_config
from .models import WebObjectsService, WebObjectsSettings

router = APIRouter(
    prefix="/web-objects"
)


@router.get("/info", response_model=WebObjectsService)
async def service_info():
    info = web_objects()
    return info


@router.get("/settings", response_model=WebObjectsSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=WebObjectsSettings)
async def save_settings(c: WebObjectsSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
