from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from .strategy_models import StrategyDescriptor
from app.chunking_strategies.base import Chunk
from app.retrieval_strategies.base import RetrievalResult

class RunRequest(BaseModel):
    doc_ids: Optional[List[str]] = None
    chunking_strategy: str
    chunking_params: Dict[str, Any] = {}
    retrieval_strategy: Optional[str] = None
    retrieval_params: Dict[str, Any] = {}
    query: Optional[str] = None
    k: int = 10

class RunStats(BaseModel):
    num_docs: int
    num_chunks: int
    time_parse_ms: int = 0
    time_chunk_ms: int = 0
    time_index_ms: int = 0
    time_retrieve_ms: int = 0
    total_ms: int = 0

class RunArtifacts(BaseModel):
    """Where to find the artifacts, allow FE to download"""
    run_id: str
    corpus_id: str                     # Ex: hash(doc_ids + content_hashes)
    chunking_signature: str            # key + params_signature
    retrieval_signature: Optional[str] = None
    chunks_path: str                   # path cache
    index_path: Optional[str] = None
    results_path: Optional[str] = None

class RunResponse(BaseModel):
    run_id: str
    stats: RunStats
    sample_chunks: List[Chunk] = []
    sample_results: Optional[RetrievalResult] = None