# app/parsers/registry.py
from typing import Type
from .pymupdf_parser import PdfPyMuPDFParser
from .txt_parser import TxtParser

PARSER_REGISTRY: dict[str, Type] = {
    ".pdf": PdfPyMuPDFParser,
    # ".txt": TxtParser,
}

def get_registered():
  return PARSER_REGISTRY.copy()