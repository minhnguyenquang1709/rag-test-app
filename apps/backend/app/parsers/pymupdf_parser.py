from .base import BaseParser
import fitz  # PyMuPDF


class PdfPyMuPDFParser:
    """"""

    def parse(self, file_path: str):
        doc = fitz.open(file_path)
        pages = []
        for page in doc:
            text = page.get_text("text")  # type: ignore[attr-defined]
            pages.append(text)
