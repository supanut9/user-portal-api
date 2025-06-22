from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import create_db_and_tables
from .profiles import router

# This lifespan function runs on startup.
# It imports the models to ensure they are registered before creating tables.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup: Ensuring all models are imported...")
    from .profiles import models
    await create_db_and_tables()
    yield
    print("Application shutdown.")



app = FastAPI(lifespan=lifespan, title="User Portal API", version="1.0")

app.include_router(router.router, prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the User Portal API!"}