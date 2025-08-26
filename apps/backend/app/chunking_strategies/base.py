from typing import Protocol, List, Dict, Any, Callable
from pydantic import BaseModel
from app.models.file_models import ParsedDoc

class Chunk(BaseModel):
    doc_id: str
    chunk_id: str
    text: str
    start_char: int
    end_char: int
    meta: Dict[str, Any] = {}
