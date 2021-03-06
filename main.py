from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from AFP.api import router as afp_router
from ApplicationServer.api import router as application_server_router
from Chat.api import router as chat_router
from FTP.api import router as ftp_router
from Mail.api import router as mail_router
from NAT.api import router as nat_router
from NFS.api import router as nfs_router
from OpenDirectory.api import router as od_router
from WebObjects.api import router as wo_router
from Xgrid.api import router as xgrid_router

app = FastAPI()

app.include_router(afp_router)
app.include_router(application_server_router)
app.include_router(chat_router)
app.include_router(ftp_router)
app.include_router(mail_router)
app.include_router(nat_router)
app.include_router(nfs_router)
app.include_router(od_router)
app.include_router(wo_router)
app.include_router(xgrid_router)

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
