from fastapi import FastAPI
from app.database import Base, engine
from app.routers import candidates
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Creates tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Candidate Management API",
    description="Recruitment pipeline management",
    version="1.0.0",
)

app.include_router(candidates.router)

@app.get("/health")
def health():
    return {"status": "ok"}