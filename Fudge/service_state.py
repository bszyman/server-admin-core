from datetime import datetime
from AFP.models import AFPService
from ApplicationServer.models import ApplicationServerService
from Chat.models import ChatService


def afp():
    s = AFPService()
    s.running = True
    s.start_time = datetime.now()

    return s


def application_server():
    s = ApplicationServerService()
    s.running = False
    s.start_time = None

    return s


def chat():
    s = ChatService()
    s.running = True
    s.start_time = datetime.now()

    return s
