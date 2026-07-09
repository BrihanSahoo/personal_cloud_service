from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.responses import FileResponse

from app.core.security import get_current_user

from app.services.file_service import (
    get_all_files,
    get_file,
    delete_file,
    get_file_path
)

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.get("/")
async def all_files(
    user=Depends(get_current_user)
):
    return await get_all_files(
        user["user_id"]
    )

@router.get("/download/{file_id}")
async def download(
    file_id:str,
    user=Depends(get_current_user)
):
    
    file = await get_file(file_id)
    
    if file is None:
        raise HTTPException(
            404,
            "File not found"
        )
    
    if file["user_id"] != user["user_id"]:
        raise HTTPException(
            403,
            "Access denied"
        )
    
    return FileResponse(
        path=get_file_path(file),
        filename=file["original_name"],
        media_type=file["content_type"]
    )



@router.get("/image/{file_id}")
async def image(
    file_id:str,
    user=Depends(get_current_user)
):
    
    file = await get_file(file_id)
    
    if file is None:
        raise HTTPException(
            404,
            "Image not found"
        )
    
    if file["user_id"] != user["user_id"]:
        raise HTTPException(
            403,
            "Access denied"
        )
        
    return FileResponse(
        get_file_path(file),
        media_type=file["content_type"]
    )
    
  
@router.delete("/{file_id}")  
async def delete(
    file_id:str,
    user=Depends(get_current_user)
):
    
    file = await get_file(file_id)
    
    if file is None:
        raise HTTPException(
            404,
            "File not found"
        )
        
    if file["user_id"] != user["user_id"]:
        raise HTTPException(
            403,
            "Access denied"
        )
    await delete_file(file_id)
    
    return {
        "message":"File deleted successfully"
    }