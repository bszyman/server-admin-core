from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class SoftwareUpdate(BaseModel):
    is_new: bool
    mirror: bool
    enable: bool
    name: str
    version: str
    size: int


class SoftwareUpdateSettings(BaseModel):
    # Settings - General
    automatically_mirror_updates_from_apple: bool = False
    automatically_enable_mirrored_updates: bool = False
    limit_bandwidth: bool = False
    bandwidth_limit: int
    bandwidth_limit_units: int = 1
    provide_updates_using_port: int

    # Settings - Updates
    updates: Optional[List[SoftwareUpdate]] = []


class SoftwareUpdateService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
    last_check: Optional[datetime]
