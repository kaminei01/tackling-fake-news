from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from socketio import ASGIApp
from api import endpoints
from socket_manager import sio
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

# Initialize FastAPI app
fastapi_app = FastAPI(
    title="Fake News Detection API",
    version="1.0.0",
    description="Detects fake news using a fine-tuned RoBERTa model with manual override."
)

# CORS configuration
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API endpoints
fastapi_app.include_router(endpoints.router)

# Wrap FastAPI app with Socket.IO
app = ASGIApp(sio, other_asgi_app=fastapi_app)
