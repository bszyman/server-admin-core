from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Queue(BaseModel):
    printer_kind: int = 1
    printers_address: str
    use_default_queue: bool = True
    queue_name: str


class PrintSettings(BaseModel):
    # Settings - General
    default_queue_for_lpr: Optional[int]

    # Settings - Logging
    archive_server_log: bool = True
    max_log_size_mb: int = 1
    log_level: int = 8

    # Settings - Queues
    queues: Optional[List[Queue]] = []


class QueueStatus(BaseModel):
    queue: Queue
    name: str
    jobs: int
    status: int
    shared_via: int


class PrintJob(BaseModel):
    id: int
    user: str
    job_name: str
    pages: int
    sheets: int
    status: int


class PrintService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
