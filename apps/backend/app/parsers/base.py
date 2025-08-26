from typing import Protocol, Dict, Any


# @TODO: add exception handling
# @TODO: add logging
# @TODO: define interfaces, types
class BaseParser(Protocol):
    def parse(self, file_path: str) -> Dict[str, Any]:
        """Parse the file at the given path and return its content as a dictionary.
        PDF supported.

        Args:
            file_path (str): Path to the file to be parsed.

        Returns:
            Dict[str, Any]: A dictionary containing the parsed content.
        """
        ...
