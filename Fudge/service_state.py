from datetime import datetime
from AFP.models import AFPService
from ApplicationServer.models import ApplicationServerService
from Chat.models import ChatService
from FTP.models import FTPService
from Mail.models import MailService
from NAT.models import NATService
from NFS.models import NFSService
from OpenDirectory.models import OpenDirectoryService
from WebObjects.models import WebObjectsService


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


def ftp():
    s = FTPService()
    s.running = True
    s.start_time = datetime.now()

    return s


def mail():
    s = MailService()
    s.running = True
    s.start_time = datetime.now()

    return s


def nat():
    s = NATService()
    s.running = False
    s.start_time = None

    return s


def nfs():
    s = NFSService()
    s.running = True
    s.start_time = datetime.now()

    return s


def open_directory():
    s = OpenDirectoryService()
    s.running = True
    s.start_time = datetime.now()

    return s


def web_objects():
    s = WebObjectsService()
    s.running = False
    s.start_time = None

    return s
