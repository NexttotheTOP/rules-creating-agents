"""Entrypoint for the FastAPI application."""

import logging
import uvicorn
from fastapi import FastAPI
from app.api import api_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
