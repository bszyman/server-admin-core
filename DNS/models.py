from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Zone(BaseModel):
    name: str
    primary_name_server: str
    primary_name_server_address: str


class SecondaryZone(BaseModel):
    name: str
    primaries: Optional[List[str]] = []


class DNSSettings(BaseModel):
    # Settings - General
    allow_zone_transfers: bool = True
    recursion: bool = True

    log_location: str
    log_level: int = 1


class DNSService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
