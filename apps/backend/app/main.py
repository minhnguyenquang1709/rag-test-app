from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    # @TODO: initialize singleton manager

    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
