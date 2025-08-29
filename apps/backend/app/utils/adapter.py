from langchain.schema import Document as LCDocument
from app.models.file_models import ParsedDocument, ParsedPage


def lc_docs_to_parsed_doc(file_path: str, lc_docs: list[LCDocument]) -> ParsedDocument:
    pages = []
    for i, doc in enumerate(lc_docs):
        text = getattr(doc, "page_content", "<FAIL>")  # or str(doc)
        metadata = getattr(doc, "metadata", {})  # or {}
        # metadata may contain page number depending on loader; fallback to index
        page_no = metadata.get("page") or metadata.get("page_number") or i
        pages.append(ParsedPage(page_number=page_no, text=text, metadata=metadata))
    return ParsedDocument(file_path=file_path, pages=pages)
