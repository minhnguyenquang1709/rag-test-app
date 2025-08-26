# app/models/file_models.py
from pydantic import BaseModel
from typing import List

class Page(BaseModel):
    page_num: int
    text: str

class ParsedDoc(BaseModel):
    doc_id: str
    filename: str
    pages: List[Page]
    text: str  # normalized full text