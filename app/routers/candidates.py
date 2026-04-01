from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models import Candidate
from app.schemas import CandidateCreate, CandidateResponse, StatusUpdate, StatusEnum
from typing import List
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/candidates", tags=["Candidates"])


@router.post("/", response_model=CandidateResponse, status_code=201)
def create_candidate(payload: CandidateCreate, db: Session = Depends(get_db)):
    try:
        existing = db.query(Candidate).filter(Candidate.email == payload.email).first()
        if existing:
            raise HTTPException(status_code=409, detail="Email already registered")
        candidate = Candidate(**payload.model_dump())
        db.add(candidate)
        db.commit()
        db.refresh(candidate)
        return candidate
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating candidate: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/", response_model=List[CandidateResponse])
def list_candidates(
    status: StatusEnum | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    try:
        query = db.query(Candidate)
        if status:
            query = query.filter(Candidate.status == status)
        return query.offset(skip).limit(limit).all()
    except Exception as e:
        logger.error(f"Error fetching candidates: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{candidate_id}/status", response_model=CandidateResponse)
def update_status(candidate_id: int, payload: StatusUpdate, db: Session = Depends(get_db)):
    try:
        candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")
        candidate.status = payload.status
        db.commit()
        db.refresh(candidate)
        return candidate
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating status: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")