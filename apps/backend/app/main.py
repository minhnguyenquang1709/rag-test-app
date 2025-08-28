from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    # @TODO: initialize singleton manager
    
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)