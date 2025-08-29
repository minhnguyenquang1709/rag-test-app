# @TODO: add logging
# @TODO: add error handling
from typing import Annotated, cast
from fastapi import APIRouter, Request, Response, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from app.services import io_service
from app.utils.registry import EPdfParserRegistry
from app.parsers.base import BaseParser
from app.utils.path import _safe_filename


router = APIRouter(prefix="/parse", tags=["Parse"])


class ParseRequestPayload(BaseModel):
    parser_key: EPdfParserRegistry | str
    file_names: list[str]


@router.post("/", status_code=status.HTTP_200_OK)
async def parse(payload: ParseRequestPayload, request: Request, response: Response):
    if not payload.file_names:
        return {"message": "No files to parse", "status": status.HTTP_400_BAD_REQUEST}

    file_names = payload.file_names
    results = []
    for file_name in file_names:
        if not _safe_filename(file_name):
            return {
                "message": f"Unsafe file name: {file_name}",
                "status": status.HTTP_400_BAD_REQUEST,
            }
        file_path = io_service.get_file_path(file_name)
        # print(f"Parsing file: {file_path} with parser: {payload.parser_key}")
        parser = cast(BaseParser, request.app.state.registries[payload.parser_key])
        result = jsonable_encoder(parser.parse(file_path))
        results.append(result)

    return {
        "message": f"Successfully parsed {len(file_names)} files.",
        "results": results,
        "status": status.HTTP_200_OK,
    }
