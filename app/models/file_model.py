from datetime import datetime
from pydantic import BaseModel

class FileModel(BaseModel):
    
    id:str
    file_name:str
    original_name:str
    size:int
    content_type:str
    uploaded_at:datetime