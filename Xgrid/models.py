from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class XgridSettings(BaseModel):
    # Settings - Agent
    enable_agent_service: bool = True
    controller_mode: int = 1
    specific_controller: int = 1
    agent_accept_tasks_mode: int = 1
    controller_authentication_type: int = 1
    controller_authentication_password: str

    # Settings - Controller
    enable_controller_service: bool = True
    client_authentication_mode: int = 1
    client_authentication_password: str
    agent_authentication_mode: int = 1
    agent_authentication_password: str


class XgridService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
