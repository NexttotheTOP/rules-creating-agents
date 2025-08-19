"""Package for authentication routers."""
import logging
from fastapi import APIRouter, HTTPException, Response, status
from app.schemas.auth import AuthRequest, TokenResponse
from app.services.supabase_client import supabase

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")  # , response_model=TokenResponse, status_code=status.HTTP_201_CREATED
async def sign_up(auth: AuthRequest, response: Response):
    """Sign up a new user and set JWT as an http-only cookie."""
    logging.info(f"Signing up user: {auth.email}")
    result = supabase.auth.sign_up(
        {
            "email": auth.email, 
            "password": auth.password
        }
    )
    if hasattr(result, "error") and result.error:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(result.error))
    #token = result.session.access_token  # type: ignore
    #response.set_cookie("access_token", token, httponly=True, secure=True, samesite="lax")
    return result # TokenResponse(access_token=token)

@router.post("/login", response_model=TokenResponse)
async def sign_in(auth: AuthRequest, response: Response):
    """Authenticate user and set JWT as an http-only cookie."""
    logging.info(f"Signing in user: {auth.email}")
    result = supabase.auth.sign_in(email=auth.email, password=auth.password)
    if hasattr(result, "error") and result.error:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail=str(result.error))
    token = result.session.access_token  # type: ignore
    response.set_cookie("access_token", token, httponly=True, secure=True, samesite="lax")
    return TokenResponse(access_token=token)
