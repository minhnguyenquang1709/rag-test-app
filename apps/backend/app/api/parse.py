# @TODO: add logging
# @TODO: add error handling
from typing import Annotated
from fastapi import APIRouter, File, UploadFile, status
from app.services import io_service
from app.parsers import parser_pymupdf


router = APIRouter(prefix="/parse", tags=["Parse"])


@router.post("/files/", status_code=status.HTTP_200_OK)
async def parse(file_path: str):
    return parser_pymupdf.parse(file_path)
