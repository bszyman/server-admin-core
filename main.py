from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from AFP.api import router as afp_router
from ApplicationServer.api import router as application_server_router
from Chat.api import router as chat_router

app = FastAPI()

app.include_router(afp_router)
app.include_router(application_server_router)
app.include_router(chat_router)

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
