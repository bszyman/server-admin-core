from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class RealmRole(BaseModel):
    name: str
    can_browse: bool
    can_author: bool


class Realm(BaseModel):
    name: str
    users: Optional[List[RealmRole]]
    groups: Optional[List[RealmRole]]


class URLRewrites(BaseModel):
    style: int
    pattern: str
    path: str


class MIMEType(BaseModel):
    mime_type: str
    suffix: str


class ContentHandler(BaseModel):
    handler: str
    suffix: str


class WebServerModule(BaseModel):
    name: str
    enabled: bool
    module_c_file: str
    module_path: str


class Website(BaseModel):
    domain_name: str
    ip_address: str
    port: int
    web_folder: str
    default_index_files: List[str]
    error_file: str
    admin_email: str

    folder_listing: bool = False
    webdav: bool = True
    cgi_execution: bool = False
    webmail: bool = False
    ssi: bool = False
    performance_cache: bool = True

    realms: Optional[List[Realm]]

    enable_access_log: bool = True
    archive_access_log_days: int
    access_log_location: str
    access_log_format: int
    access_log_format_other: Optional[str]

    archive_error_log_days: int
    error_log_location: str
    error_log_level: int = 4

    enable_tls: bool = False
    ssl_log_file_location: str
    certificate: Optional[int]

    aliases = List[str]
    url_rewrites = Optional[List[URLRewrites]]


class WebSettings(BaseModel):
    # Settings - General
    max_simultaneous_connections: int = 500
    connection_timeout: int = 300
    min_spare_servers: int = 1
    max_spare_servers: int = 5
    number_servers_to_start: int = 1

    # Settings - Sites
    allow_persistent_connections: bool = False
    max_persistent_connections: int = 500
    persistent_connection_timeout: int = 15

    mime_types: List[MIMEType]
    content_handlers: List[ContentHandler]

    enable_weblogs: bool = True
    default_blog_theme: int = 4
    weblog_folder: str
    email_domain: str

    enable_proxy: bool
    control_access_to_proxy: bool
    allowed_domain: str
    max_cache_size_mb: int = 1
    cache_folder: str
    blocked_hosts: Optional[List[str]]

    modules: List[WebServerModule]


class WebService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
