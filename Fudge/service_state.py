from datetime import datetime
from AFP.models import AFPService
from Chat.models import ChatService


def afp():
    s = AFPService()
    s.running = True
    s.start_time = datetime.now()

    return s


def chat():
    s = ChatService()
    s.running = True
    s.start_time = datetime.now()

    return s
