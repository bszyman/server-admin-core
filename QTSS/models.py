from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Relay(BaseModel):
    relay_name: str
    enable_relay: bool = True
    relay_type: int = 1
    relay_source_ip: str
    relay_path: str


class RelayDestination(BaseModel):
    destination_ip_address: str
    destination_type: int = 1
    udp_base_port_number: int = 5000
    multicast_ttl: int = 16

    relay: Relay


class IPBinding(BaseModel):
    bind: bool = True
    ip_address: str
    dns_name: str


class QTSSSettings(BaseModel):
    # Settings - General
    media_directory: str
    max_connections: int = 1000
    max_throughput: int = 100
    max_throughput_unit: int = 1

    # Settings - Access
    mp3_broadcast_password: str
    accept_incoming_broadcasts: bool = True
    enable_home_directory_streaming: bool = False
    enable_web_based_administration: bool = False

    # Settings - IP Bindings
    streaming_mode: int = 1
    enable_streaming_port_80: bool = False
    ip_bindings: Optional[List[IPBinding]] = []

    # Settings - Relays

    # Settings - Logging
    enable_error_log: bool = True
    archive_error_log: int = 7
    enable_access_log: bool = True
    archive_access_log: int = 7


class QTSSConnections(BaseModel):
    # 1 = user; 2 = relay
    client_type: int = 1
    type: int
    ip_address: str
    bit_rate: int
    bytes_sent: int
    percent_packet: int
    time: int
    path: str


class QTSSService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]

