# app/core/storage.py
import json, hashlib
from pathlib import Path
from typing import Any
from .config import settings

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def save_json(p: Path, obj: Any) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def load_json(p: Path) -> Any:
    return json.loads(p.read_text(encoding="utf-8"))

def raw_path(filename: str) -> Path:
    return settings.RAW_DIR / filename

def parsed_path(doc_id: str) -> Path:
    return settings.PARSED_DIR / f"{doc_id}.json"

def chunk_cache_path(strategy: str, params_hash: str, doc_id: str) -> Path:
    return settings.CHUNKS_DIR / strategy / params_hash / f"{doc_id}.json"

def result_path(run_id: str) -> Path:
    return settings.RESULTS_DIR / f"{run_id}.json"