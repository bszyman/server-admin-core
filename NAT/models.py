from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ExternalNIC(BaseModel):
    nic_name: str


class NATSettings(BaseModel):
    # Settings - General
    ip_forwarding_mode: str = "1"
    external_network_interface: int = 1


class NATService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
