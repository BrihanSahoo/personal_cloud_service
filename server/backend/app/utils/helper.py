import uuid
from pathlib import Path

IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/jpg",
    "image/webp",
    "image/gif"
}

def generate_filename(filename:str):
    extension = Path(filename).suffix
    return f"{uuid.uuid4().hex}{extension}"

def is_image(content_type:str):
    return content_type in IMAGE_TYPES