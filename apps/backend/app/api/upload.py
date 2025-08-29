# @TODO: add logging
# @TODO: add error handling
from pathlib import Path
from typing import Annotated
from fastapi import APIRouter, File, Request, UploadFile
from app.services import io_service
from app.utils.storage_scanner import scan_storage, backend_base


router = APIRouter(prefix="/upload", tags=["Upload"])


# @router.post("/file/")
# async def receive_file(file: UploadFile = File(...)):
#     if not file:
#         return {"message": "No file uploaded"}

#     io_service.save_file(file)
#     return {"message": f"Successfully uploaded {file.filename}."}


@router.post("/files/")
async def receive_files(files: Annotated[list[UploadFile], File()], request: Request):
    if not files:
        return {"message": "No files uploaded"}

    for file in files:
        io_service.save_file(file)

    # update storage index
    request.app.state.storage_index = scan_storage(backend_base)
    return {"message": f"Successfully uploaded {len(files)} files."}
