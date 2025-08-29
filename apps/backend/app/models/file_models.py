from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Any


class ParsedPage(BaseModel):
    page_number: Optional[int] = None
    text: str
    metadata: dict[str, Any] = {}


class ParsedDocument(BaseModel):
    file_path: str
    pages: list[ParsedPage] = []


class FileInfo(BaseModel):
    name: str
    path: str
    size: int
    mtime: datetime


class StorageIndex(BaseModel):
    raw_docs: list[FileInfo] = []
    parsed_docs: list[FileInfo] = []
    chunks: list[FileInfo] = []
    results: list[FileInfo] = []
