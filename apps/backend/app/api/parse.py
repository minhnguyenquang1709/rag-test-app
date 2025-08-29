# @TODO: add logging
# @TODO: add error handling
from typing import Annotated, cast
from fastapi import APIRouter, File, Request, UploadFile, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from app.services import io_service
from app.parsers import parser_pymupdf
from app.utils.registry import EPdfParserRegistry
from app.parsers.base import BaseParser


router = APIRouter(prefix="/parse", tags=["Parse"])


class ParseRequestPayload(BaseModel):
    parser_key: EPdfParserRegistry | str
    file_names: list[str]


@router.post("/", status_code=status.HTTP_200_OK)
async def parse(payload: ParseRequestPayload, request: Request):
    if not payload.file_names:
        return {"message": "No files to parse"}

    file_names = payload.file_names
    results = []
    for file_name in file_names:
        file_path = io_service.get_file_path(file_name)
        # print(f"Parsing file: {file_path} with parser: {payload.parser_key}")
        parser = cast(BaseParser, request.app.state.registries[payload.parser_key])
        result = jsonable_encoder(parser.parse(file_path))
        results.append(result)

    return {"message": f"Successfully parsed {len(file_names)} files.", "results": results}