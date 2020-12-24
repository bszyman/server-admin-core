from fastapi import APIRouter
from Fudge.service_state import chat
from .actions import read_config, save_config
from .models import ChatService, ChatSettings

router = APIRouter(
    prefix="/chat"
)


@router.get("/info", response_model=ChatService)
async def service_info():
    info = chat()
    return info


@router.get("/settings", response_model=ChatSettings)
async def get_settings():
    config = read_config()
    return config


@router.post("/settings", response_model=ChatSettings)
async def save_settings(c: ChatSettings):
    config = save_config(c)
    #apply_config()
    #restart_service()
    return config
