from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class WebObjectsSettings(BaseModel):
    # Settings - General
    wotaskd_port: int = 1085
    monitor_port: int = 56789
    turn_monitor_on: bool = False


class WebObjectsService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
