from app.core.singleton import SingletonMetaclass
from app.utils.registry import EPdfParserRegistry, register
from .base import BaseParser
from app.utils.adapter import lc_docs_to_parsed_doc

# import fitz  # PyMuPDF
from langchain_community.document_loaders import PyMuPDFLoader


class PdfPyMuPDFParser(BaseParser, SingletonMetaclass):
    """A parser that uses PyMuPDF to extract text from PDF files."""

    def parse(self, file_path: str):
        # doc = fitz.open(file_path)
        loader = PyMuPDFLoader(file_path, mode="page")
        docs = loader.load()

        return lc_docs_to_parsed_doc(file_path=file_path, lc_docs=docs)


parser_pymupdf = PdfPyMuPDFParser()
register(EPdfParserRegistry.PYMUPDF_PARSER.value, parser_pymupdf)
