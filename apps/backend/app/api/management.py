# @TODO: add logging
# @TODO: add error handling
from typing import Annotated
from fastapi import APIRouter, File, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.services import io_service


router = APIRouter(prefix="/manage", tags=["Manage"])


@router.get("/storage")
async def get_storage(request: Request):
    json_compatible_storage_index = jsonable_encoder(request.app.state.storage_index)
    return JSONResponse(content=json_compatible_storage_index)
