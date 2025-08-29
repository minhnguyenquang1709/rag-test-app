def _safe_filename(name: str) -> bool:
    # basic guard: prevent path separators / parent traversal
    return "/" not in name and "\\" not in name and ".." not in name and name.strip() != ""