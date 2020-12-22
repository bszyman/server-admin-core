from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date, time


class Certificate(BaseModel):
    common_name: str
    organization: str
    organization_unit: str
    city: str
    state: str
    country_code: str
    valid_from: date
    expires_on: date
    private_key_passphrase: str
    authority: str


class ServiceAccess(BaseModel):
    name: str
    users: Optional[List[str]]
    groups: Optional[List[str]]


class ServerOverviewSettings(BaseModel):
    # Settings - General
    enable_ntp: bool = True
    enable_snmp: bool = False
    enable_ssh: bool = True

    serial_number: str
    registered_to: str
    organization: str

    # Settings - Network
    computer_name: str
    local_hostname: str

    # Settings - Date & Time
    set_date_time_automatically: bool
    date: Optional[date]
    time: Optional[time]
    timezone: str

    # Settings - Certificates
    certificates: Optional[List[Certificate]] = []

    # Settings - Access
    use_same_access_for_all_services: bool = True
    allow_mode: int = 1
    services: Optional[List[ServiceAccess]]


class Interface(BaseModel):
    name: str
    family: str
    ip_address: str
    dns_name: str


class Volumes(BaseModel):
    name: str
    capacity: str
    available: str
    percent_free: str


class ServerActivity(BaseModel):
    cpu_usage: int
    network_traffic: int


class ServerOverviewService(BaseModel):
    system_version: str
    server_version: str
    computer_name: str
    local_hostname: str
    default_appletalk_zone: str
    license_type: str
    start_time: Optional[datetime]
