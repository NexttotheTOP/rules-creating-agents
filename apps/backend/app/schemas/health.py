from pydantic import BaseModel

class HealthResponse(BaseModel):
    """Model for health check responses."""
    status: str
