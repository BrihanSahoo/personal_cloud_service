from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from app.services.file_service import upload_file
from app.core.security import get_current_user

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

async def upload(
    file:UploadFile = File(...),
    user=Depends(get_current_user),
):
    
    result = await upload_file(
        file=file,
        user_id=user["user_id"],
    )
    
    if result is None:
        raise HTTPException(
            status_code=413,
            detail="Maximum upload size is 100MB"
        )
    return result