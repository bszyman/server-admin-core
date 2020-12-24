from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AFPSettings(BaseModel):
    # Settings - General
    enable_rendezvous_registration: bool = True
    enable_browsing_with_appletalk: bool = True
    do_not_send_same_greeting_twice: bool = False
    encoding_for_older_clients: int = 1
    logon_greeting: Optional[str] = None

    # Settings - Access
    authentication: int = 1

    enable_guest_access: bool = False
    enable_secure_connections: bool = True
    enable_administrator_to_masq: bool = True

    client_connections: str = "1"
    client_connections_limit: int = 1000
    guest_connections: str = "1"
    guest_connections_limit: int = 1000

    # Settings - Logging
    enable_access_log: bool = False
    access_archive_every: bool = True
    access_archive_every_days: int = 7
    event_login: bool = True
    event_logout: bool = True
    event_open_file: bool = True
    event_create_file: bool = True
    event_create_folder: bool = True
    event_delete: bool = True

    error_archive_every: bool = True
    error_archive_every_days: int = 7

    # Settings - Idle Users
    allow_clients_to_sleep: bool = True
    allow_clients_to_sleep_hours: int = 24
    disconnect_idle_users: bool = False
    disconnect_idle_users_minutes: int = 10

    disconnect_except_guests: bool = True
    disconnect_except_administrators: bool = True
    disconnect_except_registered_users: bool = True
    disconnect_except_open_files: bool = True

    disconnect_message: Optional[str] = None


class AFPConnection(BaseModel):
    name: str
    status: str
    address: str
    connected: str
    idle_for: str


class AFPService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
