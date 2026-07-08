from datetime import datetime,timedelta
from jose import jwt,JWTError
from passlib.context import CryptContext
from fastapi import Depends,HTTPException
from fastapi.security import HTTPBearer

from app.core.config import (
    JWT_ALGORITHM,
    JWT_SECRET,ACCESS_TOKEN_EXPIRE_MINUTES
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

security = HTTPBearer()

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(password:str,hashed:str):
    return pwd_context.verify(password,hash=hashed)

def create_access_token(data:dict):
    payload = data.copy()
    
    expire = datetime.utcnow()+timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    
    payload.update(
        {
            "exp":expire
        }
    )
    
    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

def get_current_user(credentials=Depends(security)):
    
    token = credentials.credentials
    
    try:
        
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )
        
        return payload
    except JWTError:
        
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )