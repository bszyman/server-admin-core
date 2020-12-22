from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class NetBootClient(BaseModel):
    host_name: str
    address: str
    hardware_address: str
    system_type: str
    client_name: str
    index: int
    last_boot_time: datetime
    image_name: str


class NetBootPort(BaseModel):
    enabled: bool
    port_name: str


class NetBootImageStorage(BaseModel):
    volume: str
    images: bool
    client_data: bool


class NetBootImage(BaseModel):
    image_name: str
    default: bool
    enable: bool
    diskless: bool
    index: int
    architecture: int
    protocol: int


class NetBootSettings(BaseModel):
    # Settings - General
    netboot_service_ports: Optional[List[NetBootPort]] = []
    netboot_image_storage: Optional[List[NetBootImageStorage]] = []
    number_of_afp_connections: int = 50

    # Settings - Images
    netboot_images: Optional[List[NetBootImage]] = []

    # Settings - Filters
    enable_netboot_dhcp_filtering: bool = False
    client_filter_mode: int = 1
    filter_hardware_addresses: Optional[List[str]] = []

    # Settings - Logging
    log_detail_level: int = 2


class NetBootService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
