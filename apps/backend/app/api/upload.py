# @TODO: implement file upload functionality
# @TODO: add logging
# @TODO: add error handling
from fastapi import APIRouter, File, UploadFile
from typing import Annotated
from apps.backend.app.services import io_service


router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/file/")
async def receive_file(file: UploadFile):
    return io_service.save_file(file)


@router.post("/files/")
async def receive_files():
    pass
