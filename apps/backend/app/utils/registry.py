from typing import Any
from enum import Enum


class EPdfParserRegistry(str, Enum):
    PYMUPDF_PARSER = "pymupdf_parser"


class EChunkingStrategy(str, Enum):
    FIXED_SIZE = "fixed_size"


_registry: dict[str, Any] = {}


def register(name: str, instance: Any):
    _registry[name] = instance
    print(f"Registered: {name}")


def get_registered() -> dict[str, Any]:
    return _registry.copy()
