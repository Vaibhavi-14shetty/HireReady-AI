from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="HireReady AI API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "HireReady AI API is running!",
        "algorithm": settings.ALGORITHM,
    }
