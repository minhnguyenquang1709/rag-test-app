from .base import BaseParser


class TxtParser:
    """"""

    def parse(self, file_path: str):
        text = open(file_path, "r", encoding="utf-8", errors="ignore").read()
        return {"pages": [{"page_num": 0, "text": text}]}
