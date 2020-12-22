from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ServiceRule(BaseModel):
    allow: bool
    description: str
    ports: List[int]
    protocol: str


class ServiceInterface(BaseModel):
    service_name: str
    service_mode: int
    service_rules: List[ServiceRule]


class AdvancedRule(BaseModel):
    enabled: bool
    number: int
    action: int
    ports: List[int]
    source: str
    destination: str


class AddressGroup(BaseModel):
    group_name: str
    addresses: Optional[List[str]]


class FirewallSettings(BaseModel):
    # Settings - General
    address_groups = List[AddressGroup]

    # Settings - Services
    interfaces = List[ServiceInterface]

    # Settings - Logging
    enable_logging: bool = True
    log_all_allowed_packets: bool = False
    log_all_denied_packets: bool = False
    log_packet_limit: int = 1000

    # Settings - Advanced
    enable_for_tcp: bool = False
    enable_for_udp: bool = False
    advanced_rules: List[AdvancedRule]


class ActiveRules(BaseModel):
    priority: int
    packets: int
    bytes: int
    rule: str


class FirewallService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
