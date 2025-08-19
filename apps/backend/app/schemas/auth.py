from pydantic import BaseModel, EmailStr


class AuthRequest(BaseModel):
    """Request model for authentication."""

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Response model for authentication tokens."""

    access_token: str
    token_type: str = "bearer"
