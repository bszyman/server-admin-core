from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FTPSettings(BaseModel):
    # Settings - General
    disconnect_client_after_login_failures: int = 3
    ftp_admin_email_address: str = "user@hostname"
    authentication_method: int = 1
    allow_maximum_authenticated_users: int = 50
    enable_anon_access: bool = False
    allow_maximum_anon_users: int = 50
    enable_mac_bin_conversion: bool = True

    # Settings - Messages
    show_welcome_message: bool = True
    welcome_message: Optional[str] = ""
    show_banner_message: bool = True
    banner_message: Optional[str] = ""

    # Settings - Logging
    log_auth_user_uploads: bool = True
    log_auth_user_downloads: bool = True
    log_auth_user_ftp_commands: bool = False
    log_auth_user_rule_violation: bool = False
    log_anon_user_uploads: bool = True
    log_anon_user_downloads: bool = True
    log_anon_user_ftp_commands: bool = False
    log_anon_user_rule_violation: bool = False

    # Settings - Advanced
    authenticated_users_see: int = 1
    ftp_root: str = ""


class FTPConnection(BaseModel):
    name: str
    type: int
    address: str
    activity: str


class FTPService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
