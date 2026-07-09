from fastapi import APIRouter,HTTPException

from app.models.user_model import (
    UserLogin,
    UserSignup
)

from app.services.auth_service import (
    login,
    signup
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/signup")
async def signup_user(user:UserSignup):
    
    user_id = await signup(user=user)
    
    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    return {
        "message" : "User created successfully",
        "user_id":user_id
    }
  
@router.post("/login") 
async def login_user(user:UserLogin):
    token = await login(user=user)
    
    if token is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )
    
    return {
        "access_token":token,
        "token_type":"bearer"
    }

