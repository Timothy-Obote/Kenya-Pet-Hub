# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from . import models
from .routers import auth, pets

# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kenya Pet Marketplace API", version="1.0.0")

# CORS — allow your frontend origin (for dev set localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # change to your frontend url or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(pets.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Kenya Pet Marketplace API",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    }
