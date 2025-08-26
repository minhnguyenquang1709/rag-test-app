# app/parsers/registry.py
from typing import Dict, Type
from .pymupdf_parser import PdfPyMuPDFParser
from .txt_parser import TxtParser

PARSER_REGISTRY: Dict[str, Type] = {
    ".pdf": PdfPyMuPDFParser,
    ".txt": TxtParser,
}
