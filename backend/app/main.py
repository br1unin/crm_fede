import os
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import Base, engine
from app.routes import auth, clients, sales, tractors, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CRM Tractores API",
    version="0.1.0",
    description="API para gestionar usuarios, clientes, tractores y ventas.",
)

allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "*")
allowed_origins: List[str]
if allowed_origins_env.strip() == "*":
    allowed_origins = ["*"]
else:
    allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(clients.router)
app.include_router(tractors.router)
app.include_router(sales.router)


@app.get("/health", tags=["health"])
def health_check() -> dict:
    return {"status": "ok"}
