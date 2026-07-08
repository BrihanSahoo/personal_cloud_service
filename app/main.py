from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.upload import router as upload_router
from app.routes.files import router as files_router

app = FastAPI(
    title="Personal file server",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(files_router)

@app.get("/")
async def root():
    return {
        "message":"File server API running"
    }