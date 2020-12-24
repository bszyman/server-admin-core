from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ApplicationServerSettings(BaseModel):
    # Settings - General
    configuration_type: str = "2"
    jboss_netboot_url: Optional[str] = None
    configuration_name: int = 1


class ApplicationServerService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
