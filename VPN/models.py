from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class NetworkRoutingDefinition(BaseModel):
    network_address: str
    network_mask: str
    network_type: int


class VPNSettings(BaseModel):
    # Settings - L2TP
    enable_l2tp: bool = False
    l2tp_starting_ip_address: str
    l2tp_ending_ip_address: str
    ppp_auth_model: int = 1
    ipsec_auth_mode: int = 1
    ipsec_shared_secret: Optional[str]
    ipsec_certificate: Optional[int]

    # Settings - PPTP
    enable_pptp: bool = False
    allow_40_bit_encryption: bool = False
    pptp_starting_ip_address: str
    pptp_ending_ip_address: str

    # Settings - Logging
    verbose_logging: bool = True

    # Settings - Client Information
    dns_servers: Optional[List[str]]
    search_domains: Optional[List[str]]
    network_routing_definitions: Optional[List[NetworkRoutingDefinition]]


class VPNConnections(BaseModel):
    username: str
    remote_ip_address: str
    internal_ip_address: str
    protocol: int
    connected_for: int


class VPNService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
    last_check: Optional[datetime]
