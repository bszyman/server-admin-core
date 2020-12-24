from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class HostDomain(BaseModel):
    domain: str


class ChatSettings(BaseModel):
    # Settings - General
    host_domains: List[HostDomain] = []
    welcome_message: str = ""
    ssl_certificate: int = 1


class ChatService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
