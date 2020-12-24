from datetime import datetime
from Chat.models import ChatService


def chat():
    s = ChatService()
    s.running = True
    s.start_time = datetime.now()

    return s
