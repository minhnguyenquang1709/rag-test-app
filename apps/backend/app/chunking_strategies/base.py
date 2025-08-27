from typing import Protocol, List, Dict, Any, runtime_checkable, Optional
from pydantic import BaseModel
from ..models.file_models import ParsedDoc


class Chunk(BaseModel):
    doc_id: str
    chunk_id: str # unique per doc

    text: str
    start_char: int  # offset in ParsedDoc.text

    end_char: int
    page_start: Optional[int] = None

    page_end: Optional[int] = None
    meta: Dict[str, Any] = {}

    # versioning
    strategy_key: str
    params_signature: str


class ChunkingStrategy(Protocol):
    key: str

    # display text and location
    def chunk(self, doc: "ParsedDoc", **params) -> List[Chunk]: ...
