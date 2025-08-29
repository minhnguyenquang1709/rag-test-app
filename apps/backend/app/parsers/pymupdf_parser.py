from app.core.singleton import SingletonMetaclass
from app.utils.registry import EPdfParserRegistry, register
from .base import BaseParser

# import fitz  # PyMuPDF
from langchain_community.document_loaders import PyMuPDFLoader


class PdfPyMuPDFParser(BaseParser, SingletonMetaclass):
    """A parser that uses PyMuPDF to extract text from PDF files."""

    async def parse(self, file_path: str):
        # doc = fitz.open(file_path)
        pages = []
        loader = PyMuPDFLoader(file_path, mode="page")
        async for page in loader.alazy_load():
            pages.append(page)
        return pages


parser_pymupdf = PdfPyMuPDFParser()
register(EPdfParserRegistry.PYMUPDF_PARSER.value, parser_pymupdf)
