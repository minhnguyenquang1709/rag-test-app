from typing import Protocol

from app.models.file_models import ParsedDocument


class BaseParser(Protocol):
    def parse(self, file_path: str) -> ParsedDocument:
        """Parse the file at the given path and return its content as a dictionary.
        PDF supported.

        Args:
            file_path (str): Path to the file to be parsed.

        Returns:
            Dict[str, Any]: A dictionary containing the parsed content.
        """
        ...
