from pathlib import Path
from datetime import datetime
from typing import List
from app.models.file_models import FileInfo, StorageIndex


def _list_files(dirpath: Path) -> List[FileInfo]:
    if not dirpath.exists():
        return []
    items = []
    for p in sorted(dirpath.iterdir()):
        if p.is_file():
            stat = p.stat()
            items.append(
                FileInfo(
                    name=p.name,
                    path=str(p.resolve()),
                    size=stat.st_size,
                    mtime=datetime.fromtimestamp(stat.st_mtime),
                )
            )
    return items


def scan_storage(backend_base: Path) -> StorageIndex:
    storage_root = backend_base / "storage"
    return StorageIndex(
        raw_docs=_list_files(storage_root / "raw_docs"),
        parsed_docs=_list_files(storage_root / "parsed_docs"),
        chunks=_list_files(storage_root / "chunks"),
        results=_list_files(storage_root / "results"),
    )


backend_base = Path(__file__).resolve().parents[2]
