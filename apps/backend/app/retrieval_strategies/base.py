from typing import Protocol, List, Dict, Any, Optional, runtime_checkable
from pydantic import BaseModel
from ..chunking_strategies.base import Chunk


class Query(BaseModel):
    query_id: str
    text: str
    filters: Dict[str, Any] = {}  # future: doc_id, section tag...


class RetrievedChunk(BaseModel):
    chunk: "Chunk"
    score: float
    rank: int


class RetrievalResult(BaseModel):
    query_id: str
    items: List[RetrievedChunk]
    meta: Dict[str, Any] = {}  # ví dụ: time_ms, k, strategy_info


class RetrievalStrategy(Protocol):
    key: str

    def build_index(self, corpus_id: str, chunks: List["Chunk"], **params) -> str: ...
    def retrieve(
        self, index_id: str, query: Query, k: int = 10, **params
    ) -> RetrievalResult: ...
