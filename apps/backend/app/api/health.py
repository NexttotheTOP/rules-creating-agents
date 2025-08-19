from fastapi import APIRouter
from app.schemas.health import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="ok")
