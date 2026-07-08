from app.core.database import users_collection
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

async def signup(user):
    
    existing = await users_collection.find_one(
        {
            "email":user.email
        }
    )
    
    if existing:
        return None
    
    data = {
        "username":user.username,
        "email":user.email,
        "password":hash_password(user.password)
    }
    
    result = await users_collection.insert_one(data)
    
    return str(result.inserted_id)


async def login(user):
    
    existing = await users_collection.find_one(
        {
            "email":user.email
        }
    )
    
    if not existing:
        return None
    
    if not verify_password(
        user.password,
        existing["password"]
    ):
        return None
    
    token = create_access_token(
        {
            "user_id":str(existing["_id"]),
            "email":existing["email"],
        }
    )
    
    return token