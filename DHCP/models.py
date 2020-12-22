from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Subnet(BaseModel):
    name: str
    starting_ip_address: str
    ending_ip_address: str
    subnet_mask: str
    network_interface: int
    router: str
    lease_time: int
    lease_time_unit: int = 1

    default_domain: str
    name_servers: str

    server_name: str
    search_base: str
    port: int
    ldap_over_ssl: bool

    wins_primary_server: str
    wins_secondary_server: str
    nbdd_server: str
    nbt_node_type: int
    netbios_scope: str


class StaticMap(BaseModel):
    ethernet_address: str
    ip_address: str
    description: str


class DHCPSettings(BaseModel):
    log_level: int = 2


class DHCPService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
