from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload_router, parse_router, management_router
from app.utils.storage_scanner import scan_storage, backend_base
from app.utils.registry import get_registered

managers = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    # @TODO: initialize singleton manager
    app.state.storage_index = scan_storage(backend_base)
    app.state.registries = get_registered()
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan, docs_url="/docs")

# CORS settings
origins = ["*"]
methods = ["*"]
headers = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

app.include_router(upload_router)
app.include_router(parse_router)
app.include_router(management_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
