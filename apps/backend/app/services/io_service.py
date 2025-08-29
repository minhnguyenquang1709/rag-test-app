from fastapi import UploadFile
from app.core.config import settings
from app.core.singleton import SingletonMetaclass


class IOService(SingletonMetaclass):
    """"""

    def __init__(self):
        pass

    def save_file(self, file: UploadFile):
        try:
            if not file.filename:
                raise ValueError("File must have a filename")
            with open(settings.RAW_DIR / file.filename, "wb") as f:
                f.write(file.file.read())
                f.close()
            file.file.close()
        except Exception as e:
            raise e

        return {
            "filename": file.filename,
            "file_size": file.size,
            "content_type": file.content_type,
        }

    def get_file_path(self, filename: str) -> str:
        return str(settings.RAW_DIR / filename)


io_service = IOService()
