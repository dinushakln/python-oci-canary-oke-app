from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(
    title="OCI DevOps Demo API",
    description="🚀 A FastAPI microservice deployed with OCI DevOps",
    version="1.0.0"
)

class RootResponse(BaseModel):
    message: str
    version: str
    namespace: str

@app.get("/", response_model=RootResponse, summary="Root Endpoint", tags=["Demo"])
def read_root():
    version = os.getenv("APP_VERSION", "0.0.1")
    namespace = os.getenv("POD_NAMESPACE", "ns-red")
    return RootResponse(
        message="💙 With Love from OCI DevOps",
        version=version,
        namespace=namespace
    )