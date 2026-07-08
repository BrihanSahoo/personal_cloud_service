import os
import aiofiles

from datetime import datetime
from bson import ObjectId
from pathlib import Path
from fastapi import HTTPException
from bson import ObjectId

from app.core.config import (
    IMAGE_FOLDER,
    FILE_FOLDER,
    MAX_UPLOAD_SIZE
)

from app.core.database import files_collection
from app.utils.helper import (
    generate_filename,
    is_image
)

CHUNK_SIZE = 1024 * 1024

async def upload_file(file,user_id):
    
    filename = generate_filename(file.filename)
    
    if is_image(file.content_type):
        save_path = IMAGE_FOLDER / filename
    else:
        save_path = FILE_FOLDER / filename
    
    size = 0
    
    async with aiofiles.open(save_path,"wb") as out:
        
        while chunk := await file.read(CHUNK_SIZE):
            
            size+=len(chunk)
            
            if size > MAX_UPLOAD_SIZE:
                await out.close
                os.remove(save_path)
                return None
            await out.write(chunk)
        
        document = {
            "user_id":user_id,
            "file_name":filename,
            "original_name":file.filename,
            "content_type":file.content_type,
            "size":size,
            "uploaded_at":datetime.utcnow()
        }
        
        result = await files_collection.insert_one(document=document)
        
        document["id"] = str(result.inserted_id)
        
        return document
    
async def get_all_files(user_id:str):
    
    files = []
    
    async for file in files_collection.find({"user_id":user_id}):
        file["id"] = str(file["_id"])
        del file["_id"]
        
        files.append(file)
    return files

async def get_file(file_id:str):
    
    file = await files_collection.find_one(
        {
            "_id":ObjectId(file_id)
        }
    )
    
    return file

def get_file_path(file):
    
    if is_image(file["content_type"]):
        return IMAGE_FOLDER / file["file_name"]

    return FILE_FOLDER / file["file_name"]

async def delete_file(file_id:str):
    
    file = await get_file(file_id)
    
    if file is None:
        return False
    
    path = get_file_path(file)
    
    if path.exists():
        path.unlink()
    
    await files_collection.delete_one(
        {
            "_id":ObjectId(file_id)
        }
    )
    
    return True