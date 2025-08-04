from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Health"])

class HealthCheck(BaseModel):
    status: str = "OK"

@router.get("/health")
async def health_check():
    return HealthCheck()