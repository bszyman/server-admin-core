from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WindowsSettings(BaseModel):
    # Settings - General
    role: int = 1
    description: str
    computer_name: str
    workgroup: str

    # Settings - Access
    allow_guest_access: bool = False
    client_connections_mode: int = 1
    client_connections_max: int = 500
    auth_ntlmv2_kerberos: bool = True
    auth_ntlm: bool = True
    auth_lan_manager: bool = True

    # Settings - Logging
    log_detail: int = 1

    # Settings - Advanced
    code_page: int = 1
    enable_workgroup_master_browser: bool = True
    enable_domain_master_browser: bool = False
    wins_registration_mode: int = 1
    wins_server: str
    enable_virtual_share_points: bool = True


class WindowsConnection(BaseModel):
    name: str
    ip_address: str
    time: int


class WindowsService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
