from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ChatSettings(BaseModel):
    # Settings - General
    host_domains: Optional[List[str]] = []
    welcome_message: str = ""
    ssl_certificate: int = 1


class ChatService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
