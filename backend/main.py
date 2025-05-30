from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from socketio import ASGIApp
from api import endpoints
from socket_manager import sio  # ✅ Import from socket_manager

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(endpoints.router)

# Wrap with Socket.IO
app = ASGIApp(sio, other_asgi_app=app)
