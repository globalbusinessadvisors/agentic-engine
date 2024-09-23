from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import get_db
from models import Employment

router = APIRouter()

class EmploymentCreate(BaseModel):
    agent_id: int
    position: str
    start_date: str
    end_date: str = None

class EmploymentResponse(BaseModel):
    id: int
    agent_id: int
    position: str
    start_date: str
    end_date: str = None

@router.post("/", response_model=EmploymentResponse)
def create_employment(employment: EmploymentCreate, db: Session = Depends(get_db)):
    db_employment = Employment(
        agent_id=employment.agent_id,
        position=employment.position,
        start_date=employment.start_date,
        end_date=employment.end_date
    )
    db.add(db_employment)
    db.commit()
    db.refresh(db_employment)
    return db_employment

@router.get("/", response_model=List[EmploymentResponse])
def read_employments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employments = db.query(Employment).offset(skip).limit(limit).all()
    return employments

@router.get("/{employment_id}", response_model=EmploymentResponse)
def read_employment(employment_id: int, db: Session = Depends(get_db)):
    employment = db.query(Employment).filter(Employment.id == employment_id).first()
    if employment is None:
        raise HTTPException(status_code=404, detail="Employment record not found")
    return employment

@router.put("/{employment_id}", response_model=EmploymentResponse)
def update_employment(employment_id: int, employment: EmploymentCreate, db: Session = Depends(get_db)):
    db_employment = db.query(Employment).filter(Employment.id == employment_id).first()
    if db_employment is None:
        raise HTTPException(status_code=404, detail="Employment record not found")
    db_employment.agent_id = employment.agent_id
    db_employment.position = employment.position
    db_employment.start_date = employment.start_date
    db_employment.end_date = employment.end_date
    db.commit()
    db.refresh(db_employment)
    return db_employment

@router.delete("/{employment_id}", response_model=EmploymentResponse)
def delete_employment(employment_id: int, db: Session = Depends(get_db)):
    db_employment = db.query(Employment).filter(Employment.id == employment_id).first()
    if db_employment is None:
        raise HTTPException(status_code=404, detail="Employment record not found")
    db.delete(db_employment)
    db.commit()
    return db_employment
