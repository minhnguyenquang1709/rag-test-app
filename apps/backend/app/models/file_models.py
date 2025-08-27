from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Page(BaseModel):
    page_num: int
    text: str
    # optional: bbox lines/blocks if need layout-aware chunking in the future

class ParsedDoc(BaseModel):
    # identity
    doc_id: str                       # hash base on filename + size/text hash
    filename: str
    source_path: Optional[str] = None 
    # content
    pages: List[Page]
    text: str                         # pages + text: retrieval needs to display the source
    # metadata
    meta: Dict[str, str] = {}         # Ex: author, created_at, mime
    # versioning
    artifact_version: int = 1
    content_hash: str                 # sha256 of full text