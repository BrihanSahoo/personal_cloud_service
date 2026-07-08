from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE = os.getenv("DATABASE")

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


STORAGE_PATH = Path(os.getenv("STORAGE_PATH"))

MAX_UPLOAD_SIZE = int(os.getenv("MAX_UPLOAD_SIZE"))

IMAGE_FOLDER = STORAGE_PATH / "images"
FILE_FOLDER = STORAGE_PATH / "files"

IMAGE_FOLDER.mkdir(parents=True,exist_ok=True)
FILE_FOLDER.mkdir(parents=True,exist_ok=True)