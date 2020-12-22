from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class NFSSettings(BaseModel):
    # Settings - General
    number_server_daemons: int = 20
    server_clients_mode: int = 1


class NFSService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
