# app/core/config.py
from pydantic import BaseModel
from pathlib import Path


class Settings(BaseModel):
    DATA_DIR: Path = Path("./storage")
    RAW_DIR: Path = DATA_DIR / "raw_docs"
    PARSED_DIR: Path = DATA_DIR / "parsed_docs"
    CHUNKS_DIR: Path = DATA_DIR / "chunks"
    RESULTS_DIR: Path = DATA_DIR / "results"

    class Config:
        env_file = ".env"


settings = Settings()
settings.RAW_DIR.mkdir(parents=True, exist_ok=True)
settings.PARSED_DIR.mkdir(parents=True, exist_ok=True)
settings.CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
settings.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
